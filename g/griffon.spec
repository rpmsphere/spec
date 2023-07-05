Name: griffon
Summary: Multilanguage IDE
Version: 1.8.4
Release: 10.1
Group: Development/Tools
License: see copyright
URL: https://griffon.lasotel.fr/en/
Source0: https://griffon.lasotel.fr/download/%{name}-%{version}.tar.gz
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXi-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  atk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libX11-devel
BuildRequires:  pango-devel
BuildRequires:  zlib-devel
BuildRequires:  gtk3-devel
BuildRequires:  vte291-devel
BuildRequires:  webkitgtk-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  libnotify-devel
BuildRequires:  python2-scons
BuildRequires:  python2

%description
Griffon is a text editor for HTML, BASH, Perl, PHP and C language...developer.
It allows the generation of source code in a few clicks avoiding traps BASH
syntax example where a single misplaced space has the power to crash a script.

%prep
%setup -q
sed -i -e 's|webkitgtk-3.0|webkit-1.0|' -e 's|file|open|' SConstruct
sed -i '44i env.MergeFlags(env.ParseFlags(["-Wl,--allow-multiple-definition"]))' SConstruct

%build
scons %{?_smp_mflags} PREFIX=/usr LIBDIR=%_libdir --install-sandbox=%{buildroot}

%install
mkdir -p  %{buildroot}%{_bindir}
install -Dm755 work/%{name} %{buildroot}%{_bindir}/%{name}
mkdir -p  %{buildroot}%{_datadir}/pixmaps/
install -Dm644 pixmaps/%{name}_icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir -p  %{buildroot}%{_datadir}/%{name}/images/
cp -a pixmaps/* %{buildroot}%{_datadir}/%{name}/images/
#install -Dm644 pixmaps/* %{buildroot}%{_datadir}/%{name}/images/
mkdir -p  %{buildroot}%{_datadir}/%{name}/autocomp/
install -Dm644 autocomp/* %{buildroot}%{_datadir}/%{name}/autocomp/
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Griffon
Comment=Editor IDE
Exec=griffon
Icon=griffon
Terminal=false
Categories=Application;Development;
Type=Application
EOF

%files
%doc COPYING README.md
%{_bindir}/%{name}
#{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Nov 30 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.4
- Rebuilt for Fedora
* Wed Dec 25 2013 Gary Richardson <garich@ptd.net> - 1.6.5
- Rebuilt for Fedora modified for scons
