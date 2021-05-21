Name:           jquery-ui
URL:            http://jqueryui.com/
Summary:        jQuery User Interface
Version:        1.11.3
Release:        1.1
License:        MIT or GPLv2+
Group:          Productivity/Networking/Web/Utilities
Source:         https://github.com/downloads/jquery/jquery-ui/%{name}-%{version}.zip
BuildArch:      noarch
Requires:       jquery-core

%description 
jQuery UI is a curated set of user interface interactions, effects, widgets,
and themes built on top of the jQuery JavaScript Library. Whether you're
building highly interactive web applications or you just need to add a date
picker to a form control, jQuery UI is the perfect choice.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/javascript/%{name}

%changelog
* Fri Feb 13 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11.3
- Rebuilt for Fedora
