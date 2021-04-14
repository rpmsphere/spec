%undefine _debugsource_packages

Name:				 stegfs
Version:			 201001
Release:			 6.1
Summary:			 FUSE based Steganographic Filesystem
Source:			 http://prdownloads.sourceforge.net/stegfs/stegfs-%{version}-src.tar.bz2
Patch1:         stegfs-fix_makefile.patch
URL:				 https://albinoloverats.net/stegfs
Group:			 System/Filesystems
License:			 GNU General Public License version 3 (GPL v3)
BuildRequires:	 fuse-devel
BuildRequires:	 mhash-devel
BuildRequires:	 libmcrypt-devel
BuildRequires:	 ncurses-devel
BuildRequires:	 gcc make glibc-devel pkgconfig

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
%__rm Makefile
%__cp Makefile.gnu Makefile
%patch1

%build
export SUSE_ASNEEDED=0
%__make %{?jobs:-j%{jobs}} \
	CC="%__cc" \
	OPTFLAGS="%{optflags} -Wall" \
	all

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__make install PREFIX="$RPM_BUILD_ROOT"
%find_lang stegfs

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files -f stegfs.lang
%doc doc/LICENCE doc/README
%{_bindir}/stegfs
%{_bindir}/mkstegfs
%doc %{_mandir}/man1/stegfs.1.*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 201001
- Rebuilt for Fedora
* Mon Jun 21 2010 pascal.bleser@opensuse.org
- initial package (201001)
