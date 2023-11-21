%undefine _debugsource_packages

Summary: A BBC BASIC interpreter for Linux
Name: brandy
Version: 1.21.17
Release: 1
License: GPLv2+
Group: Development/Tools
#URL: https://sourceforge.net/projects/brandy/
Source: https://brandy.matrixnetwork.co.uk/releases/MatrixBrandy-%{version}.tar.gz
URL: https://brandy.matrixnetwork.co.uk/
BuildRequires: SDL-devel

%description
Brandy is an interpreter for BBC BASIC V that runs under a variety
of operating systems. Basic V is the version of BASIC supplied
with desktop computers running RISC OS. These were originally made
by Acorn Computers but are now designed and manufactured by
companies such as Advantage Six and Castle Technology.

Matrix Brandy is this fork, forked from David Daniels' Sourceforge
release version 1.20.1. Developed on a CentOS 6 32-bit machine,
tested by me on CentOS 6 64-bit, CentOS 7 and a Raspberry Pi.
Graphics is handled using the SDL 1.2 library.

%prep
%setup -q -n MatrixBrandy-%{version}
sed -i 's|-Wall|-Wall -fPIE|' makefile

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc COPYING READ.ME docs/*.txt examples
%{_bindir}/brandy

%changelog
* Fri Jan 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.21.17
- Rebuilt for Fedora
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.19-6
- fix license tag
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.19-5
- Autorebuild for GCC 4.3
* Thu Sep 14 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.0.19-4
- rebuild
* Wed Aug 16 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.0.19-3
- Added perl hack for proper flags going to gcc (Thanks Tibbs)
* Sun Aug 13 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.0.19-2
- Fix for examples being correctly copied
- altered %%doc
- corrected initial import date
- added %%defattr
* Thu Aug 10 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.0.19-1
- Initial import into FE
