Name:           glyr
Version:        0.9.9
Release:        7.1
License:        GPL-3.0+
Summary:        Search eninge for Musicrelated Metadata
URL:            https://github.com/sahib/glyr
Group:          Productivity/Networking/Web/Utilities
Source0:        https://github.com/downloads/sahib/%{name}/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE glyr-0.9.9-date-n-time.patch lazy.kent@opensuse.org -- remove __DATE and __TIME__ that causes the package to rebuild when not needed
Patch0:         glyr-0.9.9-date-n-time.patch
# PATCH-FIX-OPENSUSE glyr-0.9.9-optflags.patch lazy.kent@opensuse.org -- use default openSUSE optimization flags.
Patch1:         glyr-0.9.9-optflags.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(sqlite3)

%description
The sort of metadata glyr is searching (and downloading) is usually the
data you see in your musicplayer. And indeed, originally it was written
to serve as internally library for a musicplayer, but has been extended
to work as a standalone program which is able to download:

* cover art;
* lyrics;
* bandphotos;
* artist biography;
* album reviews;
* tracklists of an album;
* a list of albums from a specific artist;
* tags, either related to artist, album or title relations, for example
  links to wikipedia;
* similar artists;
* similar songs.

%package -n libglyr
Summary:        Searcheninge for Musicrelated Metadata
Group:          System/Libraries

%description -n libglyr
Glyr shared library.

The sort of metadata glyr is searching (and downloading) is usually the
data you see in your musicplayer. And indeed, originally it was written
to serve as internally library for a musicplayer, but has been extended
to work as a standalone program which is able to download:

* cover art;
* lyrics;
* bandphotos;
* artist biography;
* album reviews;
* tracklists of an album;
* a list of albums from a specific artist;
* tags, either related to artist, album or title relations, for example
  links to wikipedia;
* similar artists;
* similar songs

%package -n libglyr-devel
Summary:        Searcheninge for Musicrelated Metadata
Group:          Development/Libraries/C and C++
Requires:       libglyr = %{version}

%description -n libglyr-devel
Glyr development files.

The sort of metadata glyr is searching (and downloading) is usually the
data you see in your musicplayer. And indeed, originally it was written
to serve as internally library for a musicplayer, but has been extended
to work as a standalone program which is able to download:

* cover art;
* lyrics;
* bandphotos;
* artist biography;
* album reviews;
* tracklists of an album;
* a list of albums from a specific artist;
* tags, either related to artist, album or title relations, for example
  links to wikipedia;
* similar artists;
* similar songs

%prep
%setup -qn %{name}
%patch0
%patch1

%build
%cmake \
%ifarch x86_64
    -DLIB_SUFFIX="64" \
%endif
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?_smp_mflags} VERBOSE=1

%install
%make_install

%post -n libglyr -p /sbin/ldconfig

%postun -n libglyr -p /sbin/ldconfig

%files
%doc AUTHORS CHANGELOG COPYING README.textile TODO
%{_bindir}/glyrc

%files -n libglyr
%doc COPYING
%{_libdir}/*.so.*

%files -n libglyr-devel
%doc src/examples
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.9
- Rebuilt for Fedora
* Mon May  7 2012 lazy.kent@opensuse.org
- Update to 0.9.9.
  * Added --as-one (and --no-as-one) option to glyrc.
  * Fixed up readme.
  * Updated help.
  * Added support for :escape: characters in --write and
  - -callback.
  * Added slothradio provider.
  * Various fixes.
- Rebase "date-n-time" and "optflags" patches.
* Fri Apr 13 2012 lazy.kent@opensuse.org
- Update to 0.9.8.
  * Fixed --musictree -> --musictree-path.
  * Updated help accordingly.
  * Fixed crash in relations:musicbrainz.
  * Fixed storing of getters with optional artist/album.
  * Added musicbrainz as cover provider.
  * Fix for -v0.
  * Added extra trimming for all text items.
  * Fixed magistrix parser.
  * Fixed incorrect trimming.
  * Fixed cover:albumart.
  * Made jamendo provider work inplace.
* Tue Mar  6 2012 lazy.kent@opensuse.org
- Corrected source URL and replaced tarball.
* Mon Mar  5 2012 lazy.kent@opensuse.org
- Update to 0.9.5.
  * Added jamendo provider.
- Added examples to devel package.
- Removed _service - use tarball.
* Wed Feb 22 2012 lazy.kent@opensuse.org
- Update from git.
  * Updated discogs provider to new use the new API.
  * Updated README.
  * Fixed typos.
  * Fixed the unicode lookup problem.
- Updated "optflags" patch.
* Fri Feb 10 2012 lazy.kent@opensuse.org
- Update from git (various fixes).
- Updated "date-n-time" patch.
* Wed Feb  8 2012 lazy.kent@opensuse.org
- Added COPYING to libglyr package.
* Sat Feb  4 2012 lazy.kent@opensuse.org
- Update to 0.9.4.
- Patch to use default openSUSE optimisation flags.
* Sun Dec 25 2011 lazy.kent@opensuse.org
- Patch to remove __DATE and __TIME__ that causes the package to
  rebuild when not needed.
* Wed Dec 14 2011 lazy.kent@opensuse.org
- Initial package created - 0.9.
