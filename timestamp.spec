Name:				timestamp
Version:			1.1
Release:			3.1
Summary:			Pipe that timestamps Lines
Source:			http://math.missouristate.edu/~erik/files/timestamp-%{version}.tar.gz
Patch1:			timestamp-rename.patch
URL:				http://math.missouristate.edu/~erik/software.php?id=95
Group:			Productivity/File utilities
License:			GNU General Public License version 2 or later (GPLv2 or later)
BuildRoot:		%{_tmppath}/build-%{name}-%{version}
BuildRequires:	gcc make glibc-devel
BuildRequires:	autoconf automake libtool

%description
Timestamp is a text filtering pipe that marks each line with a timestamp. The
time is set when the first character of the line is received, and the util is
capable of coping with CR repeats fairly well (won't over-write or update the
timestamp).

Authors:
--------
    Erik Greenwald <erik@smluc.org>

%prep
%setup -q
%__mv ts.1 timestamp.1
%patch1

%build
autoreconf -fiv
%configure
%__make %{?jobs:-j%{jobs}}

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/timestamp
%doc %{_mandir}/man1/timestamp.1*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora

* Wed Nov 21 2007 Pascal Bleser <guru@unixtech.be> 1.1
- initial version
