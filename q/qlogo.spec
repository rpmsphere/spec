%global _name QLogo
%undefine _debugsource_packages

Name:		qlogo
Version:	0.92
Release:	5.1
Summary:	A cross-platform rewrite of the UCBLogo language
License:	GPLv2
Group:		Development/Languages
Source0:	https://codeload.github.com/jasonsikes/QLogo/tar.gz/v%{version}#/%{_name}-%{version}.tar.gz
URL:		https://github.com/jasonsikes/QLogo
BuildRequires:	qt5-qtbase-devel
BuildRequires:  ImageMagick

%description
QLogo is an interpreter for the Logo language written in C++ using
Qt and OpenGL. Specifically, it mimics (as reasonably as possible)
the UCBLogo interpreter developed at U.C. Berkeley.

%prep
%setup -q -n %{_name}-%{version}

%build
%qmake_qt5 %{_name}.pro
make

%install
%__rm -rf $RPM_BUILD_ROOT
install -Dm755 %{_name} $RPM_BUILD_ROOT%{_bindir}/%{name}

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=QLogo
Comment=A cross-platform rewrite of the UCBLogo language
Exec=qlogo
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Development;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert icon.ico $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Sep 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.92
- Rebuilt for Fedora
