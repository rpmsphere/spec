%undefine _debugsource_packages

Name: beebeep
Summary: Secure Network Chat
Version: 5.8.6
Release: 1
Group: Applications/Communications
URL: https://sourceforge.net/projects/beebeep/
Source0: https://sourceforge.net/projects/beebeep/files/Sources/%{name}-code-%{version}.zip
License: Qt Public License
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: desktop-file-utils

%description
BeeBEEP is a secure network chat. You can talk and send files with all your
friends inside a local area network such of an office, home or internet cafe
without a server.

%prep
%setup -q -n %{name}-code-r1557

%build
qmake-qt5 -recursive
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mv test/%{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_libdir}
cp -a test/* %{buildroot}%{_libdir}
install -Dm 0644 src/images/beebeep.png \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
  --set-icon=%{name} scripts/debian_amd64/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc *.txt
%{_bindir}/%{name}
%{_libdir}/lib*
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/applications/beebeep.desktop

%changelog
* Fri May  3 2024 Martin RS - 5.8.6
- add desktop and icon files
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 5.8.6
- Rebuilt for Fedora
