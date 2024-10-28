Name:                           ploticus
Version:                        2.42
%define pkg_version 242
Release:                        13.1
Summary:                        Ploticus Data Display Engine
Source:                 https://prdownloads.sourceforge.net/ploticus/%{name}%{pkg_version}_src.tar.gz
Patch0:                 ploticus242.patch
URL:                            https://ploticus.sourceforge.net
Group:                  Productivity/Graphics/Visualization/Graph
License:                        GNU General Public License (GPL)
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel libjpeg-devel gd-devel giflib-devel bison flex
BuildRequires:  freetype-devel make gcc glibc-devel

%description
A free, GPL, non-interactive software package for producing plots, charts, and
graphics from data. It was developed in a Unix/C environment and runs on
various Unix, Linux, and win32 systems.

ploticus is good for automated or just-in-time graph generation, handles date
and time data nicely, and has basic statistical capabilities. It allows
significant user control over colors, styles, options and details.

%prep
%setup -q -n %{name}%{pkg_version}
%patch 0 -p1

%build
%__make -C src \
        %{?jobs:-j%{jobs}} \
        LIB="%{_lib}" \
        CC="%__cc %{optflags} -Wno-format-security" \
        NOSWFFLAG="" \
        PREFABS_DIR="%{_libdir}/ploticus"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 src/pl "$RPM_BUILD_ROOT%{_bindir}/%{name}"
%__install -d "$RPM_BUILD_ROOT%{_libdir}/%{name}"
%__rm prefabs/README
%__cp prefabs/* "$RPM_BUILD_ROOT%{_libdir}/%{name}/"

%files
%doc src/GPL.txt src/README
%{_bindir}/%{name}
%{_libdir}/%{name}

%changelog
* Mon Apr 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.42
- Rebuilt for Fedora
* Wed Mar 11 2009 Pascal Bleser <pascal.bleser@opensuse.org> 2.41-0.pm.1
- updated in-tree ming to 0.4.2
- update to 2.41
* Sun Apr 13 2008 Pascal Bleser <guru@unixtech.be> 2.40-0.pm.1
- new upstream version
- bumped in-tree ming version to latest 0.4.0.beta5
- moved to openSUSE Build Service
* Fri Sep 15 2006 Pascal Bleser <guru@unixtech.be> 2.33-1
- new package
