%if 0%{?suse}
%global bash_completionsdir /usr/share/bash-completion/completions/
%else
%global bash_completionsdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo '/etc/bash_completion.d')
%endif

# Disable stripping of binaries because of https://github.com/crystal-lang/crystal/issues/10948
%global __os_install_post %{nil}

Name:           crystal
Version: 1.2.0
Release:        3.bin
Provides:       crystal1.1
Conflicts:      crystal
%if 0%{?fedora} || 0%{?rhel}
License:        ASL 2.0
%else
License:        Apache-2.0
%endif
Summary:        A programming language for humans and computers
Url:            https://github.com/crystal-lang/crystal
Source0:        https://github.com/crystal-lang/crystal/archive/refs/tags/%{version}.tar.gz
Source1:        https://github.com/crystal-lang/crystal/releases/download/%{version}/crystal-%{version}-docs.tar.gz
Source100:      https://github.com/crystal-lang/crystal/releases/download/%{version}/crystal-%{version}-1-linux-x86_64.tar.gz
#Source101:	crystal-%{version}-1-linux-aarch64.tar.gz
Requires: gcc
Requires: glibc
Requires: pkgconfig
Requires: pcre-devel
Requires: libevent-devel
%if ! 0%{?rhel}
Recommends: libssl-devel, libz-devel, libxml2-devel, libgmp-devel, libyaml-devel
%endif

%description
Crystal is a general-purpose, object-oriented programming language.
 With syntax inspired by Ruby, it is a compiled language with static type-checking,
 serving both, humans and computers.

%package docs
Summary: Documentation for the Crystal Programming Language
BuildArch: noarch
%description docs
%{summary}.

%package samples
Summary: Sample code for the Crystal Programming Language
BuildArch: noarch
%description samples
%{summary}.

%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}

%prep
%setup -q -n crystal-%{version}
%setup -q -b 1 -n crystal-%{version}-docs
%ifarch x86_64
%setup -q -b 100 -n crystal-%{version}-1
%endif
%ifarch %{ix86}
%setup -q -b 101 -n crystal-%{version}-1
%endif

%build

%install
%if "%{_lib}" == "lib64"
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/crystal <<-SH
#!/bin/sh

# Wrapper script to set CRYSTAL_LIBRARY_PATH and CRYSTAL_PATH
# This is necessary because the default library path doesn't match the path
# on this system.

export CRYSTAL_LIBRARY_PATH=\${CRYSTAL_LIBRARY_PATH-"%{_libdir}/crystal"}
export CRYSTAL_PATH=\${CRYSTAL_PATH-"lib:%{_datadir}/crystal/src"}
exec %{_libdir}/crystal/crystal "\$@"
SH
chmod 0755 %{buildroot}%{_bindir}/crystal

install -D -m 0755 bin/crystal %{buildroot}%{_libdir}/crystal/crystal
%else
install -D -m 0755 bin/crystal %{buildroot}%{_bindir}/crystal
%endif

mkdir -p %{buildroot}%{_libdir}/crystal
cp -r lib/crystal/lib*\.* %{buildroot}%{_libdir}/crystal

install -D -m 0644 share/man/man1/crystal.1.gz %{buildroot}%{_mandir}/man1/crystal.1.gz
install -D -m 0644 share/licenses/crystal/LICENSE %{buildroot}%{_datadir}/crystal/LICENSE

# install -D -m 644 etc/completion.bash {buildroot}{bash_completionsdir}/crystal
# install -D -m 644 etc/completion.zsh {buildroot}{_datadir}/zsh/site-functions/_crystal

mkdir -p %{buildroot}%{_datadir}/crystal
cp -r share/crystal/src %{buildroot}%{_datadir}/crystal
cp -r ../crystal-%{version}-docs %{buildroot}%{_datadir}/crystal/docs
cp -r ../crystal-%{version}/samples %{buildroot}%{_datadir}/crystal

install -D -m 0755 bin/shards %{buildroot}%{_bindir}/shards
install -D -m 0644 share/man/man1/shards.1.gz %{buildroot}%{_mandir}/man1/shards.1.gz
install -D -m 0644 share/man/man5/shard.yml.5.gz %{buildroot}%{_mandir}/man5/shard.yml.5.gz

%check
%if "%{_lib}" == "lib64"
%{buildroot}%{_libdir}/crystal/crystal --version
%else
%{buildroot}%{_bindir}/crystal --version
%endif

%files
%doc %{_datadir}/crystal/LICENSE
%{_bindir}/crystal
%dir %{_libdir}/crystal
%{_libdir}/crystal/*
%{_mandir}/man1/crystal.1.gz
# {bash_completionsdir}/{name}
# {_datadir}/zsh/site-functions/_{name}
%dir %{_datadir}/crystal
%dir %{_datadir}/crystal/*
%{_datadir}/crystal/src/*
%{_bindir}/shards
%{_mandir}/man1/shards.1.gz
%{_mandir}/man5/shard.yml.5.gz

%files docs
%dir %{_datadir}/crystal/docs/
%{_datadir}/crystal/docs/*

%files samples
%dir %{_datadir}/crystal/samples/
%{_datadir}/crystal/samples/*

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
* Wed Oct 13 2021 Johannes Müller <straightshoota@gmail.com>
- Release 1.2.0
* Mon Jul 26 2021 Johannes Müller <straightshoota@gmail.com>
- Release 1.1.1
* Wed Jul 14 2021 Johannes Müller <straightshoota@gmail.com>
- Update to crystal 1.1.0
* Mon Apr 26 2021 Johannes Müller <straightshoota@gmail.com>
- Initial package setup
