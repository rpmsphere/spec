%global debug_package %{nil}

Name:           darts
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
License:        LGPL-2.1+
Group:          System/Libraries
Version:        0.31
Release:        70.1
URL:            http://cl.aist-nara.ac.jp/~taku-ku/software/darts/
Source0:        http://chasen.org/~taku/software/darts/src/darts-%version.tar.bz2
Summary:        Double Array Trie System

%description
Darts is a simple C++ template library to construct Double-Arrays [Aoe
1989]. Double-Arrays are data structures to represent Trie. These are
faster than other Trie implementations.

Darts is used by Chasen.

Authors:
--------
    Taku Kudoh <taku-ku@is.aist-nara.ac.jp>

%prep
%setup -q

%build
rm -f config.cache
autoreconf --force --install
CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=/usr \
            --libdir=%{_libdir} \
	    --libexecdir=%{_libdir} \
            --mandir=%{_mandir} \
            --infodir=%{_infodir}

#            %{_target_cpu}-suse-linux
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPY* ChangeLog README*
%{_includedir}/*
%{_libdir}/%{name}

%changelog
* Mon Jul 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.31
- Rebuild for Fedora
* Thu Dec  1 2011 coolo@suse.com
- add automake as buildrequire to avoid implicit dependency
* Wed Dec 12 2007 uli@suse.de
- update -> 0.31 (required by new chasen)
  - license change (LGPL -> dual LGPL/BSD)
  - lots of entirely undocumented changes
* Sat Mar 31 2007 rguenther@suse.de
- add zlib-devel BuildRequires
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue May  4 2004 hmacht@suse.de
- added norootforbuild in specfile
* Tue Sep  9 2003 schwab@suse.de
- Add workaround for gcc bug.
* Mon Aug 25 2003 ro@suse.de
- remove /usr/include from filelist
* Mon Aug 25 2003 mfabian@suse.de
- new package: darts 0.2.
