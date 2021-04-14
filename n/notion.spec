Name:               notion
Version:            3.2019050101
%define pkg_version %(echo %{version}|tr . -)
Release:            1
Summary:            Free Tiling Tabbed Window Manager
Source:             https://github.com/raboof/notion/archive/%{pkg_version}.tar.gz#/%{name}-%{pkg_version}.tar.gz
Source1:            notion.desktop
URL:                https://notionwm.net/
Group:              System/GUI/Other
License:            GNU Lesser General Public License version 2.1 or later (LGPL v2.1 or later)
BuildRequires:      libX11-devel
BuildRequires:      libXext-devel
BuildRequires:      libSM-devel
BuildRequires:      libXinerama-devel
BuildRequires:      libXrandr-devel
BuildRequires:      lua-devel

%description
Notion is a tiling, tabbed window manager for the X window system.
Features include:
* Workspaces: each workspace has its own tiling
* Multihead: the mod_xinerama plugin provides very nice dual-monitor support
* RandR: mod_xrandr picks up changes in the xrandr configuration without the
  need for restarting Notion (read this, though)
* Extensibility: Notion can be extended with lua scripts. Browse through the
  scripts collection

%prep
%setup -q -n %{name}-%{pkg_version}
sed -i 's|return lua_sethook(\(.*\));|lua_sethook(\1);return TRUE;|' libextl/luaextl.c

%build
%__make %{?_smp_flags} \
    CC="gcc" \
    OPTFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    ETCDIR="%{_sysconfdir}/%{name}" \
    SHAREDIR="%{_datadir}/%{name}" \
    MANDIR="%{_mandir}" \
    DOCDIR="%{_docdir}/%{name}" \
    INCDIR="%{_includedir}/%{name}" \
    LIBDIR="%{_libdir}" \
    LUA_DIR="%{_usr}" \
    X11_PREFIX="%{_usr}" \
    X11_LIBDIR="%{_usr}/%{_lib}" \
    HAS_SYSTEM_ASPRINTF=1

%install
%__make \
    CC="gcc" \
    OPTFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    ETCDIR="%{_sysconfdir}/%{name}" \
    SHAREDIR="%{_datadir}/%{name}" \
    MANDIR="%{_mandir}" \
    DOCDIR="%{_docdir}/%{name}-%{version}" \
    INCDIR="%{_includedir}/%{name}" \
    LIBDIR="%{_libdir}" \
    LUA_DIR="%{_usr}" \
    X11_PREFIX="%{_usr}" \
    X11_LIBDIR="%{_usr}/%{_lib}" \
    HAS_SYSTEM_ASPRINTF=1 \
    DESTDIR="%{buildroot}" \
    install

%__install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/xsessions/%{name}.desktop"

%find_lang %name
LF="$PWD/%name.lang"
pushd "%{buildroot}%{_mandir}"
/bin/ls -1d */man1 | while read x; do
    l="${x%%/*}"
    l="${l%%/*}"
    echo "%doc %dir %lang($l) %{_mandir}/${l}" >>"$LF"
    echo "%doc %dir %lang($l) %{_mandir}/${l}/man1" >>"$LF"
done
/bin/ls -1 */man1/*.1* | while read x; do
    l="${x%%/*}"
    l="${l%%/*}"
    f="${x##*/}"
    echo "%doc %lang($l) %{_mandir}/${l}/man1/$f*" >>"$LF"
done
popd

%clean
%__rm -rf %{buildroot}

%files -f %name.lang
%{_datadir}/doc/%{name}-%{version}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*.lua
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
%{_datadir}/xsessions/%{name}.desktop

%changelog
* Thu Oct 31 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2019050101
- Rebuilt for Fedora
* Fri Oct 26 2012 toganm@opensuse.org
- Update to version 3+2012042300
- Use lua51 explicitly for opensuse >= 12.1
- There is no changes file in the sources file, probably the best
  changes file is located at the git
  http://notion.git.sourceforge.net/git/gitweb.cgi?p=notion/notion;a=log;h=91414f3a55bad7929562d3c3486c39e82b6418d2
* Tue Nov  1 2011 pascal.bleser@opensuse.org
- add xsession desktop file for notion
* Tue Nov  1 2011 pascal.bleser@opensuse.org
- initial version (3+2011102900)
