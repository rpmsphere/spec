Name:           js-brython
URL:            https://www.brython.info/
Summary:        A Python 3 implementation for client-side web programming
Version:        3.3.0
Release:        2.1
License:        MIT
Group:          Productivity/Networking/Web/Utilities
Source:         Brython-%{version}.tar.gz
BuildArch:      noarch

%description 
Brython is designed to replace Javascript as the scripting language for the Web.
As such, it is a Python 3 implementation (you can take it for a test drive
through a web console), adapted to the HTML5 environment, that is to say with an
interface to the DOM objects and events.

%prep
%setup -q -n Brython-%{version}

%install
install -d $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}

%files
%{_datadir}/javascript/%{name}

%changelog
* Wed Jan 04 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 3.3.0
- Rebuilt for Fedora
