#BuildRequires: /usr/bin/desktop-file-install libgtk+2-devel perl(IO/Handle.pm)
%define commit  7cae89f
%define uname   puzzles

Name:           sgt-%{uname}
Version:        20161228
Release:        1
Summary:        Simon Tatham's one-player puzzle collection
Group:          Games/Puzzles
License:        MIT
URL:            http://www.chiark.greenend.org.uk/~sgtatham/puzzles/
Source0:        http://www.chiark.greenend.org.uk/~sgtatham/puzzles/%{uname}-%{version}.%{commit}.tar.gz
Source1:        template.desktop
Patch0:         puzzles-20160104-mga-no-Werror.patch
BuildRequires:  pkgconfig(gtk+-3.0)
Source44: import.info

%description
This is a collection of small desktop toys, little games that you can
pop up in a window and play for two or three minutes while you take a
break from whatever else you were doing.

%prep
%setup -q -n %{uname}-%{version}.%{commit}
%patch0 -p1
iconv -f ISO88591 -t UTF8 < LICENCE > LICENSE

%build
autoreconf -vfi
%configure --bindir=%{_bindir}
%make_build

%install
%makeinstall
install -d %{buildroot}%{_datadir}/applications

# Rename binaries, install icons and create desktop files
path=%{buildroot}%{_bindir}
for game in ${path}/*; do
    base=`basename ${game}`
    name=`perl -e 'print ucfirst($ARGV[0])' "${base}"`
    command=puzzle-${base}

    mv ${game} ${path}/puzzle-${base}

    sed -e "s/<NAME>/${name}/g;s!<EXEC>!${command}!g;s!<ICON>!${command}!g" %{_sourcedir}/template.desktop > puzzle-${base}.desktop
    desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ ${command}.desktop

    for size in 16 32 48; do
        install -D -m644 icons/${base}-${size}d24.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/${command}.png
    done
done

# Create a menu subfolder for Simon Tatham's puzzles in the Puzzle folder
mkdir -p %{buildroot}%{_datadir}/desktop-directories
cat > %{buildroot}%{_datadir}/desktop-directories/%{name}.directory <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Simon Tatham's Puzzles
Icon=puzzle_section
Type=Directory
EOF

mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
cat > %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged/%{name}.menu <<EOF
<!DOCTYPE Menu PUBLIC "-//freedesktop//DTD Menu 1.0//EN"
"http://www.freedesktop.org/standards/menu-spec/menu-1.0.dtd">
<Menu>
  <Name>Applications</Name>
  <Menu>
    <Name>Games</Name>
    <Menu>
      <Name>Puzzles</Name>
      <Menu>
        <Name>Simon Tatham's Puzzles</Name>
        <Directory>%{name}.directory</Directory>
        <Include>
          <Category>X-SGTatham-Puzzles</Category>
        </Include>
      </Menu>
    </Menu>
  </Menu>
</Menu>
EOF

%files
%doc HACKING LICENSE puzzles.txt
%{_datadir}/applications/puzzle-*.desktop
%{_datadir}/desktop-directories/%{name}.directory
%{_gamesbindir}/puzzle-*
%{_datadir}/icons/hicolor/*/apps/puzzle-*.png
%{_sysconfdir}/xdg/menus/applications-merged/%{name}.menu

%changelog
* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 20161029-alt1_1
- update by mgaimport
* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 20160429-alt1_1
- update by mgaimport
* Tue Jun 07 2016 Igor Vlasenko <viy@altlinux.ru> 20160410-alt1_1
- converted for ALT Linux by srpmconvert tools
