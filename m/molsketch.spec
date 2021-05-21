Name:           molsketch
Version:        0.3.0
Release:        10.1
Summary:        Molecular Structures Editor
License:        GPL-2.0
Group:          Productivity/Scientific/Chemistry
URL:            http://molsketch.sourceforge.net
Source0:        http://sourceforge.net/projects/molsketch/files/Molsketch/Lithium%20%{version}/Molsketch-%{version}-src.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  kdelibs-devel
BuildRequires:  openbabel-devel
BuildRequires:  qca2

%description
molsKetch is a molecular structures editor for KDE.
  
%prep
%setup -q -n Molsketch-%{version}

%build
sed -i 's|/usr/local|/usr|' CMakeLists.txt
%cmake .
make

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
#doc CHANGELOG COPYING INSTALL
%{_bindir}/molsketch
%{_libdir}/lib*.so*
%{_datadir}/molsketch
%{_datadir}/doc/molsketch
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/*

%changelog
* Wed Jan 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuilt for Fedora
* Sat Jul  7 2012 scorot@free.fr
- fix build on SLE 11
* Sat Jul  7 2012 scorot@free.fr
- fix openbabel dependency according to package name changes
* Sat Feb 25 2012 mailaender@opensuse.org
- update to version 2.0.0 with fixes from git by the developer
* Tue Feb 21 2012 mailaender@opensuse.org
- initial packaging, added QtAssistant include path to CMakeLists.txt, added BuildRequires: -post-build-checks because of compiler warnings
