%define __python /usr/bin/python2
%undefine _debugsource_packages
%define _libdir %{_prefix}/lib

Name:                            mcm
Version:                         0.9.3
Release:                         9.1
Summary:                         Monocaffe Connections Manager
# https://launchpad.net/mcm/trunk/%{version}/+download/mcm-%{version}.tar.gz
Source:                  mcm-%{version}.tar.bz2
Patch1:                  mcm-fix_desktop_file.patch
Patch2:                  mcm-placeholders.patch
URL:                             https://launchpad.net/mcm
Group:                   Productivity/Networking/SSH
License:                         GNU General Public License version 3 (GPL v3)
BuildRequires:   python
BuildRequires:   fdupes
BuildArch:               noarch
Requires:                pygtk2
Requires:                gtk-vnc-python
Requires:                pyxdg
Requires:                vte
Requires:                libxml2-python

%description
Monocaffe Connections Manager is a set of tools to ease the management of
several servers. It's aimed at network or system administrators who need to
connect every day to different servers by different means. It can be used via
an ncurses interface without requiring an X server, and it can be used via a
GNOME-based GUI.

%prep
%setup -q
%patch 1
%patch 2
sed -i 's|/usr/share/apps/|/usr/lib/|' bin/mcm

%__rm -rf ./dist
%__rm -rf *.sh
%__mkdir_p .rpmdocs
%__mv doc/[A-Z]* .rpmdocs/
for f in .rpmdocs/*; do
         [ -e "$f" ] || continue
         test -s "$f" || %__rm "$f"
done
%__mkdir_p .man
%__mv doc/*.[1-9] .man/

find . -name '.*.swo' -exec %__rm {} \;

%__rm i18n/generate_pot.py
%__rm i18n/generate_mo.sh
%__rm i18n/messages.mo

%build
%__awk '/^\+\+\+ / {print $2}' <"%{PATCH2}" | while read f; do
         %__sed -i '
                  s|@@PYTHON@@|%__python|g
                  ;
                  s|@@LIBDIR@@|%{_libdir}/%{name}|g
         ' "$f"
done

%install
%__install -d "$RPM_BUILD_ROOT%{_libdir}/%{name}"
%__cp -a * "$RPM_BUILD_ROOT%{_libdir}/%{name}/"
sed -i 's|/usr/bin/python |/usr/bin/python2 |' "$RPM_BUILD_ROOT%{_libdir}/%{name}/bin/%{name}"

%__install -d "$RPM_BUILD_ROOT%{_bindir}"
relpath=$(python2 -c 'import os; print os.path.relpath("%{_libdir}/%{name}/bin", "%{_bindir}")')
%__ln_s "$relpath/mcm" "$RPM_BUILD_ROOT%{_bindir}/mcm"
%__ln_s "$relpath/mcm" "$RPM_BUILD_ROOT%{_bindir}/mcm-gtk"

%__install -d "$RPM_BUILD_ROOT%{_datadir}/applications"
%__mv "$RPM_BUILD_ROOT%{_libdir}/%{name}/gtk/mcm.desktop" "$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop"

%__install -d "$RPM_BUILD_ROOT%{_datadir}/pixmaps"
relpath=$(python2 -c 'import os; print os.path.relpath("%{_libdir}/%{name}/gtk", "%{_datadir}/pixmaps")')
%__ln_s "$relpath/mcm_icon.png" "$RPM_BUILD_ROOT%{_datadir}/pixmaps/mcm.png"

for f in .man/*; do
         [ -e "$f" ] || continue
         m="${f##*.}"
         b="${f##*/}"
         %__install -D -m0644 "$f" "$RPM_BUILD_ROOT%{_mandir}/man${m}/$b"
done

%files
%doc .rpmdocs/*
%{_bindir}/mcm
%{_bindir}/mcm-gtk
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/mcm.png
%doc %{_mandir}/man*/*.*.*
%{_libdir}/%{name}

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.3
- Rebuilt for Fedora

* Tue May 11 2010 pascal.bleser@opensuse.org
- initial package (0.9.3)
