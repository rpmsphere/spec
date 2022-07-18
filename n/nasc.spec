%define app_id com.github.parnold-x.nasc

Name:           nasc
Version:        0.5.4
Release:        1
License:        GPL-3.0
Group:          Applications/Engineering
URL:            https://parnold-x.github.io/nasc
Summary:        Do maths like a normal person
Source0:        https://github.com/parnold-x/nasc/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.28.0
BuildRequires:  pkgconfig(cln)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(libsoup-2.4)
#Requires:       qalculate
Provides:       %{app_id} = %{?epoch:%{epoch}:}%{version}-%{release}

# https://fedoraproject.org/wiki/Packaging:Scriptlets
# https://fedoraproject.org/wiki/PackagingDrafts/ScriptletSnippets
Requires(post):         coreutils
Requires(postun):       coreutils
Requires(posttrans):    coreutils
# gtk-update-icon-cache
#Requires(post):         gtk-update-icon-cache
Requires(postun):       gtk-update-icon-cache
Requires(posttrans):    gtk-update-icon-cache
# update-mime-database
#Requires(post):         shared-mime-info
#Requires(postun):       shared-mime-info
#Requires(posttrans):    shared-mime-info
# update-desktop-database
Requires(post):         desktop-file-utils
Requires(postun):       desktop-file-utils
#Requires(posttrans):    desktop-file-utils
# glib-compile-schemas
#Requires(post):         glib2
Requires(postun):       glib2
Requires(posttrans):    glib2
# ldconfig

%description
This is an application where you do calculations "like a normal
person". It lets you type whatever you want, smartly figures out what
computations are needed, and outputs an answer on the right pane.
Then you can plug those answers in to future equations and if that
answer changes, so does the equations it is used in.

%prep
%setup -q
sed -i '8i using namespace std;' libqalculatenasc/QalculateNasc.cc

%build
%cmake .
%cmake_build

%install
%cmake_install
ln -s %{app_id} %{buildroot}%{_bindir}/%{name}

%post
/bin/touch --no-create "%{_datadir}/icons/hicolor" &> /dev/null || :
#/usr/bin/update-mime-database -n "%{_datadir}/mime" &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
if [[ "${1}" -eq "0" ]]; then
  /usr/bin/glib-compile-schemas "%{_datadir}/glib-2.0/schemas" &> /dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :
if [[ "${1}" -eq "0" ]]; then
  /bin/touch --no-create "%{_datadir}/icons/hicolor" &> /dev/null || :
  /usr/bin/gtk-update-icon-cache "%{_datadir}/icons/hicolor" &> /dev/null || :
  #/usr/bin/update-mime-database -n "%{_datadir}/mime" &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas "%{_datadir}/glib-2.0/schemas" &> /dev/null || :
/usr/bin/gtk-update-icon-cache "%{_datadir}/icons/hicolor" &> /dev/null || :
#update-mime-database -n "%{_datadir}/mime" &>/dev/null || :

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{app_id}
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}.??g
%{_metainfodir}/%{app_id}.appdata.xml
%{_datadir}/qalculate/styles/*

%changelog
* Thu Dec 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.4
- Rebuilt for Fedora
* Sat Feb 16 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-12
- Update patches
* Fri Feb 15 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-11
- Improve Meson port
* Fri Feb 15 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-10
- Fix Meson port
* Fri Feb 15 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-9
- Change GenericName to Desktop calculator
* Fri Feb 15 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-8
- Fix gschema path
- Improve desktop patch
* Fri Feb 15 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-7
- Change Application ID
- Fix desktop patch
* Thu Feb 14 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-6
- Rewrite Meson patches
- Use Meson everywhere
* Thu Feb 14 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-5
- Move com.github.parnold-x.nasc.gschema.xml to data subdirectory
- Rename src/config.vala.cmake to src/config.vala.in
- Use CMake everywhere
* Sun Feb 10 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-4
- Reorganize patches
- CMake: Remove deprecated Vala option: --thread
- Meson: Add cln dependency to libqalculatenasc
- Use Meson everywhere
* Sat Feb 09 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-3
- Add sheet_path patch: use get_user_data_dir() instead of hardcoded path
- Add desktop patch: update Categories, add StartupWMClass and StartupNotify
- Add appdata patch: fix release notes, add screenshot captions and kudos
- Add symlink: nasc
* Sat Feb 09 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-2
- Fix linking on EL < 8 and FC < 28
* Sat Feb 09 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.1-1
- Update to 0.5.1
* Sat Feb 09 2019 Tomasz Tomasik <scx.mail@gmail.com> - 0.5.0-1
- Initial packaging
