%undefine _debugsource_packages
Name:           gplanarity
%define svnrev  15153
Version:        0.0.%{svnrev}
Release:        1
URL:            https://web.mit.edu/xiphmont/Public/gPlanarity.html
License:        GPL v2
Group:          Amusements/Games/Board/Puzzle
Summary:        Puzzle game involving untangling planar graphs
Source:         planarity-svn-%{svnrev}.tar.bz2
Source1:        %{name}.desktop
BuildRequires:  gtk2-devel cairo-devel freetype-devel desktop-file-utils

%description
gPlanarity is a simple puzzle game involving untangling planar graphs for fun and prizes.
If you tend to get addicted to cute little math puzzles, this one is a doozy.

%prep
%setup -q -n planarity
cp %{SOURCE1} .
touch gettext.h
echo '#define _(x) (x)' >> gettext.h
echo '#define __(x) (x)' >> gettext.h
sed -i -e 's|--static||' -e 's|-O2|-O2 -lm|' Makefile

%build
make %{?jobs:-j%jobs} DISABLE_NLS=true

%install
install -D -m 0755 gPlanarity $RPM_BUILD_ROOT%{_bindir}/gplanarity
install -D -m 0644 gPicon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/gplanarity.png
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cp %{name}.desktop %{buildroot}%{_datadir}/applications/

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%files
%doc COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.15153
- Rebuilt for Fedora
* Wed Oct 22 2008 Wind <yc.yan@ossii.com.tw>
- Rebuild for OSSII.
* Tue Aug  5 2008 prusnak@suse.cz
- created package (svn rev 15153)
