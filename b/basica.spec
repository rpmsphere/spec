%undefine _debugsource_packages

Name:               basica
Version:            1.0
Release:            3.1
Summary:            BASIC Advanced
Source:             Basica-master.zip
URL:                https://github.com/Abderasoft/Basica
Group:              Development/Languages
License:            open source

%description
Thaigasoft BASICA by Ballagyr.

%prep
%setup -q -n Basica-master

%build
export CXXFLAGS="-std=c++14 -fPIC -fPIE"
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

%changelog
* Fri Oct 19 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
