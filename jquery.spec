Name:           jquery
URL:            http://jquery.com/
Summary:        Fast and concise JavaScript Library
Version:        1.11.1
Release:        1.1
License:        MIT or GPLv2+
Group:          Productivity/Networking/Web/Utilities
Source:         http://code.jquery.com/%{name}-%{version}.min.js
BuildArch:      noarch
Provides:       jquery-core

%description 
jQuery is a fast and concise JavaScript Library that simplifies HTML
document traversing, event handling, animating, and Ajax
interactions for rapid web development. jQuery is designed to change
the way that you write JavaScript.

%prep
%setup -Tc

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}/%{name}-%{version}.min.js
ln -s %{name}-%{version}.min.js $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}/%{name}.min.js
ln -s %{name}-%{version}.min.js $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}/%{name}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/javascript/%{name}

%changelog
* Fri Oct 17 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11.1
- Rebuild for Fedora
* Sun Jun 5 2011 Ludwig Nussel <lnussel@suse.de>
- new package version 1.6.1
