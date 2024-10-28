%undefine _debugsource_packages

Name:           stegfs
Version:        2022.02.25
Release:        1
Summary:        FUSE based Steganographic Filesystem
Source:         stegfs.git.tar.bz2
Patch1:         stegfs-fix_makefile.patch
URL:            https://albinoloverats.net/stegfs
Group:          System/Filesystems
License:        GNU General Public License version 3 (GPL v3)
BuildRequires:  fuse-devel
BuildRequires:  mhash-devel
BuildRequires:  libmcrypt-devel
BuildRequires:  ncurses-devel
BuildRequires:  gcc make glibc-devel pkgconfig

%description
stegfs is a Fuse based file system which provides absolute security.
Using encryption to secure files, and the art of steganography to
hide them, stegfs aims to ensure that the existence of such files
isn't guaranteed. Implemented as a Fuse based file system and using
the mhash and mcrypt libraries to provide the cryptographic hash and
symmetric block cipher functions, stegfs is at the cutting edge of
secure file system technology.

%prep
%setup -q -n stegfs
#__rm Makefile
#__cp Makefile.gnu Makefile
#patch1

%build
export SUSE_ASNEEDED=0
%__make %{?jobs:-j%{jobs}} \
        CC="%__cc" \
        OPTFLAGS="%{optflags} -Wall" \
        all

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__make install PREFIX="$RPM_BUILD_ROOT"
#find_lang stegfs

%files
%doc docs/LICENCE docs/README docs/COPYRIGHT docs/FORMAT docs/CHANGELOG
%{_bindir}/stegfs
%{_bindir}/mkstegfs
%doc %{_mandir}/man1/*.1.*

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2022.02.25
- Rebuilt for Fedora
* Mon Jun 21 2010 pascal.bleser@opensuse.org
- initial package (201001)
