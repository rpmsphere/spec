Name:           jquery-selectBox
URL:            https://github.com/claviska/jquery-selectBox
Summary:        A styleable replacement for SELECT elements
Version:        1.1.4
Release:        2.1
License:        MIT or GPLv2+
Group:          Productivity/Networking/Web/Utilities
Source:         claviska-jquery-selectBox-v1.1.4-0-g1114755.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       jquery-core

%description 
A jQuery plugin for replacing <select> elements.

%prep
%setup -n claviska-jquery-selectBox-1114755

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/javascript/%{name}

%changelog
* Sun Oct 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.4
- Rebuilt for Fedora
