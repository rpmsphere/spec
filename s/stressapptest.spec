Name:           stressapptest
Version:        1.0.9
Release:        3
Summary:        Stressful application test
License:        Apache-2.0
Group:          System/Benchmark
URL:            https://github.com/stressapptest/stressapptest
Source:         https://github.com/stressapptest/stressapptest/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++

%description
Stressful Application Test (or stressapptest, its unix name) tries to maximize
randomized traffic to memory from processor and I/O, with the intent of
creating a realistic high load situation in order to test the existing
hardware devices in a computer.

%prep
%setup -q

%build
autoreconf -fvi
export CXXFLAGS="%{optflags} -DNDEBUG -DCHECKOPTS"
%configure \
  --disable-silent-rules \
  --disable-default-optimizations \
  --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc NOTICE
%{_bindir}/%{name}
%{_mandir}/man1/stressapptest.1*

%changelog
* Wed Aug 26 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.9
- Rebuilt for Fedora
* Thu Aug 30 2018 Tomáš Chvátal <tchvatal@suse.com>
- Format with spec-cleaner
- Use proper upstream tarball from github
- Add working URL pointing to github
* Thu Aug 30 2018 frede@b1-systems.de
- update to version 1.0.9 release
* Thu Feb  5 2015 seiler@b1-systems.de
- update to version 1.0.7 (checkout from git)
  changes: https://code.google.com/p/stressapptest/source/list
- spec file cleanup
* Mon Oct 19 2009 bitshuffler #suse@irc.freenode.org
- Initial RPM
