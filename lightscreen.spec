%global debug_package %{nil}

Name:           lightscreen
Version:        0.3
#Version:        2.4
Release:        14.1
License:        GPL
URL:            https://github.com/ckaiser/Lightscreen
Group:          Application/System
Summary:        Program to take screenshots
Source:		    %{name}-source.tar.gz
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++, qt4-devel

%description
Lightscreen is a program to take screenshots, designed to be very customizable and lightweight.

%prep
%setup -q -n %{name}-source

%build
qmake-qt4
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall INSTALL_ROOT=/$RPM_BUILD_ROOT/usr
install -Dp %{name} $RPM_BUILD_ROOT/usr/bin/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Wed Jan 2 2008 TI_Eugene <ti.eugene@gmail.com> 0.3-1.fc7
- Initial release for Fedora 7
