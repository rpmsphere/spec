%define breq qt5-qtbase-devel
%define qmake /usr/bin/qmake-qt5
%define lrelease /usr/bin/lrelease-qt5

Name:           juffed
Version:        0.10
Release:        1167
License:        GPL
URL:            https://sourceforge.net/projects/juffed/
#Source:                %{name}-%{version}-%{release}.tar.bz2
Source:         %{name}-master.zip
Group:          Utility
Summary:        Simple tabbed text editor
BuildRequires:  %{breq}
BuildRequires:  qscintilla-qt5-devel
BuildRequires:  enca-devel
BuildRequires:  gcc-c++ cmake
BuildRequires:  qtermwidget-devel

%description
Simple tabbed text editor with syntax highlighting for C++, Python, HTML, PHP,
XML, TeX, Makefiles, ini-files and patch-files

%prep
%setup -q -n %{name}-master

%build
%cmake . -DQSCINTILLA_INCLUDE_DIR=/usr/include/qt5 -DQSCINTILLA_LIBRARY=/usr/lib64/libqscintilla2_qt5.so
%cmake_build

%install
%{__rm} -rf %{buildroot}
#{makeinstall} FAKE_ROOT=%{buildroot}
%cmake_install

%files
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_libdir}/%{name}
%{_libdir}/libjuff*

%changelog
* Sun Mar 26 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10
- Rebuilt for Fedora
* Thu Apr 24 2008 TI_Eugene <ti.eugene@gmail.com> 0.2.1-1
- Initial build on OBS
* Thu Apr 24 2008 TI_Eugene <ti.eugene@gmail.com> 0.2.1-1
- Initial build on OBS
