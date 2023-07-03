Name:           screen-message
Summary:        Displays a short text fullscreen
Version:        0.25
Release:        1
License:        GPLv2+
URL:            https://darcs.nomeata.de/screen-message/
Group:          Applications/Text
BuildRequires:  gtk2-devel 
Source0:        %{name}-%{version}.tar.gz
Provides:       sm

%description
Screen Message will display a given multi-line message as large as possible,
fullscreen and black on white. You can specify the text either when launching sm,
or edit it while the program is running.

It is useful to send messages across a room, e.g. during an university lecture.
For fast startup, it is recommended to bind it to a key in your Desktop Environment.

%prep
%setup -q
sed -i -e 's|@BINPATH@/||' -e 's|sm|%{name}|' sm.desktop.in

%build
%configure
make
rename sm %{name} *

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -Dm644 %{name}.6 $RPM_BUILD_ROOT%{_datadir}/man/man6/%{name}.6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.Win32 %{name}.html %{name}.py
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/man/man6/%{name}.6*

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.25
- Rebuilt for Fedora
