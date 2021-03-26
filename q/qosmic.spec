%global debug_package %{nil}

Summary:	Graphical interface for creating flam3 fractal images
Name:		qosmic
Version:	1.5.0
#Version:	1.6.0
Release:	20.1
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2
Group:		Graphics
URL:		http://code.google.com/p/qosmic/
BuildRequires:	flam3-devel, libxml2-devel
BuildRequires:	gcc-c++, libjpeg-devel, qt4-devel
BuildRequires:	lua-devel
BuildRequires:	compat-lua-devel

%description
Qosmic is graphical interface for creating, editing, and rendering
flam3 fractal images. The electricsheep screen saver has been gaining
popularity, and Qosmic was developed to provide a Qt interface for
people interested in creating and contributing sheep.

%prep
%setup -q
sed -i 's|3\.0\.1|3.0|' %{name}.pro
sed -i 's|flam3 lua|flam3 lua-5.1|' %{name}.pro

%build
qmake-qt4
make

%install
%__rm -rf $RPM_BUILD_ROOT
%__install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc README* changes.txt COPYING
%_bindir/%{name}

%changelog
* Sun Oct 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.0
- Rebuild for Fedora
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.8-2mdv2011.0
+ Revision: 614676
- the mass rebuild of 2010.1 packages
* Fri Dec 18 2009 Lev Givon <lev@mandriva.org> 1.4.8-1mdv2010.1
+ Revision: 480013
- Update to 1.4.8.
* Sun May 10 2009 Lev Givon <lev@mandriva.org> 1.4.4-1mdv2010.0
+ Revision: 374071
- Update to 1.4.4.
* Tue Jan 13 2009 Lev Givon <lev@mandriva.org> 1.4.2-1mdv2009.1
+ Revision: 328856
- import qosmic
