%global debug_package %{nil}

Name:           quickterminal
Version:        0.0.1git
Release:        1
Summary:        Lightweight terminal emulator in Qt
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/trollixx/quickterminal
Source0:        %{name}-master.zip
BuildRequires:  qt5-devel
BuildRequires:  qtermwidget-devel

%description
Lightweight terminal emulator depending on Qt5, QTermWidget.

%prep
%setup -q -n %{name}-master
sed -i -e 's|utilities-terminal|%{name}|' -e 's|qt|%{name}|' desktop/%{name}.desktop

%build
qmake-qt5
make %{?_smp_mflags}

%install
%make_install
install -Dm755 qt %{buildroot}%{_bindir}/%{name}
install -Dm644 src/icons/application-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm644 desktop/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Jan 17 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1git
- Rebuild for Fedora
