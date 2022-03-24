Name: complexshutdown
Summary: A script to shutdown, restart, logoff or standby your computer after a specific time. With a lot of settings.
Version: 0.5
Release: 1
Group: doc
License: Free Software
Source0: %{name}_%{version}_all.deb
BuildArch: noarch

%description
A more or less simple skript, written in fpc, then rewritten in python. Main
purpose of this tool is to turn off your computer after a specific time, but
it's more complex: You can specify when to do what action with a lot of extra
options. Everything is packed in a simple and intuitive graphical user interface.

%prep
%setup -Tc

%build
ar -x %{SOURCE0}

%install
mkdir -p %{buildroot}
tar xf data.tar.gz -C %{buildroot}

%files
%{_bindir}/%{name}.py
%{_bindir}/%{name}.ui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/sounds/%{name}

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
