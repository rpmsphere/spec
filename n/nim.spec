# figure out why --debugger:native does not work with *-debuginfo packets
%define __nim_common_opts -d:release
%define __nim_harden_config() \
  for file in %*; do \
    echo "gcc.options.always %= \\"\\${gcc.options.always} ${CFLAGS:-%optflags}\\"" >> $file; \
    echo "gcc.options.linker %= \\"\\${gcc.options.linker} ${LDFLAGS:-%__global_ldflags}\\"" >> $file; \
  done

%global bashcompdir     %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%global bashcomproot    %(dirname %{bashcompdir} 2>/dev/null)

Name:           nim
Version:        1.6.12
Release:        1
Summary:        Statically typed, imperative programming language
# compiler is MIT, nimble package manager is BSD
License:        MIT and BSD
URL:            https://nim-lang.org
#ExclusiveArch:  %{nim_arches}

Source0:        https://nim-lang.org/download/%{name}-%{version}.tar.xz
Source1:        nim.1
Source2:        nimgrep.1
Source3:        nimble.1
Source4:        nimsuggest.1

Patch1:         nim-0001-allow-to-override-directories-in-install-script.patch
Patch2:         nim-0002-use-_datadir-for-platform-independent-library-path.patch
#Patch3:         nim-0003-use-versioned-source-links-in-docs.patch
#Patch4:         nim-0004-fix-compiler-binary-lookup-in-docgen.patch
Patch6:         nim-0005-Fix-async-SSL-tests.patch


# Default gcc options in nim.conf include hardened specs
Requires:       redhat-rpm-config
# Currently compiler uses C sources as intermediate representation
Requires:       gcc

BuildRequires:  nim-srpm-macros
BuildRequires:  gcc openssl-devel
BuildRequires:  pkgconfig(bash-completion)

# test dependencies
BuildRequires:  gc-devel

%if ! (0%{?rhel} && 0%{?rhel} <= 7)
Recommends: %{name}-tools%{_isa} = %{version}-%{release}
# for using --gc:boehm
Suggests: gc-devel
Suggests: %{name}-docs = %{version}-%{release}
%endif

%description
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).

%package tools
Summary:    Tools for Nim programming language
%description tools
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).

This package provides various tools, which help Nim programmers.

%package doc
Summary:    Documentation for Nim programming language
BuildArch:  noarch
%description doc
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).

This package provides documentation and reference manual for the language
and its standard library.

%prep
%autosetup -p1
#%setup -q

%build
# build bootstrap compiler
./build.sh

%__nim_harden_config compiler/nim.cfg
%__nim_harden_config config/nim.cfg

# build the koch management tool
./bin/nim compile %{__nim_common_opts} koch
# build a new version of the compiler
./koch boot %{__nim_common_opts} -d:useLinenoise
# build tools
./koch tools %{__nim_common_opts}

# generate documentation
./koch docs
sed -i '/<link.*fonts.googleapis.com/d' doc/html/*.html

rm -rf examples install.sh lib/pure/unidecode/gen.py
# generate installer script
./koch geninstall %{__nim_common_opts}

%install
sh install.sh \
  %{buildroot}%{_bindir} \
  %{buildroot}%{_sysconfdir} \
  %{buildroot}%{_datadir} \
  %{buildroot}%{_docdir} \
  %{buildroot}%{_datadir}

install -Dp -m755 bin/nim{ble,grep,suggest,pretty} %{buildroot}%{_bindir}
install -Dp -m644 tools/nim.bash-completion %{buildroot}%{bashcompdir}/nim
install -Dp -m644 dist/nimble/nimble.bash-completion %{buildroot}%{bashcompdir}/nimble
install -Dp -m644 -t%{buildroot}%{_mandir}/man1 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4

mkdir -p %{buildroot}%{_docdir}/%{name}/html
cp -a doc/html/*.html %{buildroot}%{_docdir}/%{name}/html/
cp tools/dochack/dochack.js %{buildroot}%{_docdir}/%{name}/
#ln -sr %{buildroot}%{_docdir}/%{name}/html/{overview,index}.html

#%check
#export PATH=$PATH:$(realpath ./bin)
#for cat in manyloc gc threads nimble-all lib io async rodfiles debugger examples dll flags
#do
#  ./koch tests --pedantic category $cat -d:nimCoroutines || (echo "$cat test category failed" &&  exit 1)
#done

%files
%license copying.txt dist/nimble/license.txt
%doc doc/readme.txt
%config(noreplace) %{_sysconfdir}/nim/*
%{_datadir}/nim/
%{_datadir}/nimble/
%{_bindir}/nim{,ble}
%{_mandir}/man1/nim{,ble}.1*
%{bashcompdir}/nim*

%files tools
%license copying.txt
%{_bindir}/nim{grep,suggest,pretty}
%{_mandir}/man1/nim{grep,suggest}.1*

%files doc
%doc %{_docdir}/nim

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.12
- Rebuilt for Fedora
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Wed Dec 11 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.0.4-1
- Update to 1.0.4
* Thu Nov 07 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.0.2-1
- Update to 1.0.2
* Fri Sep 27 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.0.0-1
- Update to 1.0.0
* Mon Jul 29 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.20.2-1
- Update to 0.20.2
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Fri May 10 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.19.6-1
- Update to 0.19.6
* Fri Feb 01 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.19.4-2
- Restore patch for fixing floats
* Fri Feb 01 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.19.4-1
- Update to 0.19.4
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Thu Oct 04 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.19.0-3
- Include nimpretty into tools package
* Tue Oct 02 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.19.0-2
- Fix configration path
* Fri Sep 28 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.19.0-1
- Update to 0.19.0
* Sun Sep 02 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.18.0-4
- Apply patch to fix async SSL tests
* Fri Aug 31 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.18.0-3
- Do not run JS tests to avoid nodejs dependency
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Sat Mar 03 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.18.0-1
- Update to upstream version 0.18.0
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Wed Jan 3 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.17.2-5
- Revert back to makefile for bootstrap compiler.
* Wed Jan 3 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.17.2-4
- Update runtime dependencies, and use build.sh instead of makefile
  to build bootstrap compiler.
* Fri Dec 1 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.17.2-3
- Do not load remote fonts in local HTML documentation
* Sat Nov 18 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.17.2-2
- Generate and install PDF documentation
* Tue Sep 26 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.17.2-1
- Initial package
