Name:				rand
Version:			1.9
Release:			2.1
Summary:			Pipe to randomize a Stream by Line or Word
# http://math.missouristate.edu/~erik/files/rand-%{version}.tar.gz
Source:			rand-%{version}.tar.bz2
URL:				http://math.missouristate.edu/~erik/software.php?id=7
Group:			Productivity/File utilities
License:			GNU General Public License version 2 or later (GPLv2 or later)
BuildRoot:		%{_tmppath}/build-%{name}-%{version}
BuildRequires:	gcc make glibc-devel
BuildRequires:	gettext gettext-devel intltool
BuildRequires:	autoconf automake libtool

%description
rand is a small tool that outputs a stream or file in random order.
It's useful for shuffling playlists, viewlists, generating unique tests, etc.

Authors:
--------
    Erik Greenwald <erik@smluc.org>

%prep
%setup -q

%build
%configure
%__make %{?jobs:-j%{jobs}}

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang rand

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files -f rand.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/rand
%doc %{_mandir}/man1/rand.1*
# not in openSUSE yet:
%dir %{_datadir}/locale/en_IE
%dir %{_datadir}/locale/en_IE/LC_MESSAGES

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9
- Rebuild for Fedora

* Tue Jun 16 2009 Pascal Bleser <pascal.bleser@opensuse.org> 1.9
- fix rpmlint on Factory

* Wed Nov 21 2007 Pascal Bleser <guru@unixtech.be> 1.9
- initial version
