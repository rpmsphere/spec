Name:		glogo
Version:	0.1.5
Release:	7.1
Summary:	Graphical LOGO Language
License:	see copyright
Group:		Development/Languages
Source0:	http://sourceforge.net/projects/g-logo/files/g-logo/g-logo_0.1-5/g-logo_0.1-5.tar.gz
Source1:	%{name}.png
URL:		http://g-logo.sourceforge.net/
BuildRequires:	gtk2-devel, gtkglext-devel, libsndfile-devel

%description
G-logo is a 3D graphics software. It has interpreter language processer
that it is like LOGO command. It is possible to draw 3DCG by inputting
easy command. It can be used for creating 3D modeling, drawing fractal,
creating an animation.

%prep
%setup -q -n g-logo-0.1-5

%build
export LIBS="-Wl,--allow-multiple-definition -lm"
./configure --prefix=/usr
make

%install
%__rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=G-Logo
Comment=Graphical LOGO Language
Exec=g-logo
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Development;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS README commands.txt COPYING
%{_bindir}/g-logo
%{_datadir}/g-logo
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/g-logo.mo
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Jul 06 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.5
- Rebuild for Fedora
