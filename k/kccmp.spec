Name:          kccmp
Version:       0.2
Release:       7.1
Summary:       A simple QT tool for comparing two linux kernel ".config" files
Group:         Graphical Desktop/Applications/Development
URL:           https://stoopidsimple.com/kccmp
Source:        https://stoopidsimple.com/files/%{name}-%{version}.tar.gz
Patch0:        %{name}-0.2-qt4.patch
License:       GPL
BuildRequires: boost-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: libICE-devel
BuildRequires: libpng-devel
BuildRequires: qt4-devel
BuildRequires: libSM-devel
BuildRequires: libstdc++-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrender-devel
BuildRequires: zlib-devel

%description
kccmp is a simple QT tool for comparing two linux kernel ".config" files.
It has the following features:
- displays the configuration variables with different values in a table form
- displays the configuration variables and values which are found in only one of the compared files

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4
#sed -i "s|-lqt|-lqt-mt|" Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m0755 kccmp $RPM_BUILD_ROOT%{_bindir}/kccmp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/kccmp
%doc README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora

* Tue Dec 14 2010 Automatic Build System <autodist@mambasoft.it> 0.2-7mamba
- automatic rebuild by autodist

* Sun Jun 13 2010 Automatic Build System <autodist@mambasoft.it> 0.2-6mamba
- automatic rebuild by autodist

* Mon Jun 08 2009 Automatic Build System <autodist@mambasoft.it> 0.2-5mamba
- automatic rebuild by autodist
- switched to qt4

* Fri Oct 19 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 0.2-4mamba
- rebuild with libboost 1.34.1

* Sat Jul 07 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 0.2-3mamba
- rebuilt against libboost-1.34.0

* Thu May 03 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 0.2-2mamba
- rebuilt

* Fri Nov 25 2005 Silvan Calarco <silvan.calarco@mambasoft.it> 0.2-1qilnx
- package created by autospec
