%define codemirror_ver 5.18.2

Summary:	A Linux clone of Notepad++
Name:		notepadqq
Version:	1.2.0
Release:	2
License:	GPLv3
Group:		Editors
URL:		http://notepadqq.altervista.org/wp/
Source0:	https://github.com/notepadqq/notepadqq/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	qmake5
BuildRequires:  qt5-qttools
BuildRequires:  qtchooser
#BuildRequires:  qt5-qtchooser

%description
Notepadqq is a Notepad++-like editor for the Linux desktop.

%prep
%setup -q
mkdir -p src/editor/libs/codemirror/mode/m4
sed -i -e "s/lib/%{_lib}/g" src/ui/ui.pro
#cd src/translations
#for i in *.ts; do
#	%{_libdir}/qt5/bin/lrelease $i
#done

%build
%qmake_qt5 PREFIX=%{_prefix} LRELEASE=lrelease-qt5 *.pro
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
ln -sf %{_libdir}/notepadqq/notepadqq-bin %{buildroot}%{_bindir}/notepadqq

%files
%doc README.md
%{_bindir}/notepadqq
%{_libdir}/notepadqq/notepadqq-bin
%{_datadir}/applications/notepadqq.desktop
%{_datadir}/icons/hicolor/*/apps/notepadqq.*g
%{_datadir}/notepadqq

%changelog
* Thu Mar 08 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuild for Fedora
