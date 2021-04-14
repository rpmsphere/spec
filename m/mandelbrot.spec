%undefine _debugsource_packages

Name: mandelbrot
Summary: GTK Mandelbrot browser
Version: 0.4.1
Release: 9.1
Group: science
License: GPLv3
URL: http://mandelbrot-gtk.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-gtk-0.4-1.tar.bz2
Source1: %{name}.png
BuildRequires: gtk3-devel
BuildRequires: libxml2-devel

%description
Multithreaded GTK Application for rendering the mandelbrot and julia-set.

%prep
%setup -q -n %{name}-gtk-0.4-1

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=GTK Mandelbrot Browser
Exec=%{name}
Terminal=false
Comment=Multithreaded GTK Application for rendering the mandelbrot and julia-set
Type=Application
Categories=Application;Graphics;
Icon=%{name}
EOF

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Mar 09 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuilt for Fedora
