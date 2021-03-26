Name:           brython
URL:            http://www.brython.info/
Summary:        A Python 3 implementation for client-side web programming
Version:        1.4
Release:        2.1
License:        MIT
Group:          Productivity/Networking/Web/Utilities
Source:         http://cdn.bitbucket.org/olemis/brython/downloads/Brython%{version}-20131221-111525.zip
BuildArch:      noarch

%description 
Brython is designed to replace Javascript as the scripting language for the Web.
As such, it is a Python 3 implementation (you can take it for a test drive
through a web console), adapted to the HTML5 environment, that is to say with an
interface to the DOM objects and events.

%prep
%setup -q -n Brython%{version}-20131221-111525

%install
install -d $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/javascript/%{name}

%files
%{_datadir}/javascript/%{name}

%changelog
* Thu Jan 09 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuild for Fedora
