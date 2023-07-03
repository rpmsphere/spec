Name:				 tsunami-udp
Version:			 1.1+41+349
Release:			 1.1
Summary:			 Fast File Transfer Protocol
Source:			 tsunami-udp-%{version}.tar.bz2
# remove that test binary from the build, it's the only thing breaking strict aliasing:
Patch1:			 tsunami-udp-do_not_build_fusereadtest.patch
URL:				 https://tsunami-udp.sourceforge.net/
Group:			 Productivity/Networking/Other
License:			 GNU General Public License version 2 or later (GPL v2 or later)
BuildRequires:	 gcc make glibc-devel
BuildRequires:	 autoconf automake libtool

%description
A fast user-space file transfer protocol that uses TCP control and UDP data for
transfer over very high speed long distance networks (≥ 1 Gbps and even 10 GE),
designed to provide more throughput than possible with TCP over the same
networks.

It is based on original Indiana University 2002 Tsunami source code but has
been significantly improved and extended.

Includes FTP-like client and server command line applications for normal file
transfers.
It has additionally been extended for high rate real-time data streaming in
eVLBI radio astronomy and geodesy (VSIB, PCEVN DAQ).

%prep
%setup -q -n tsunami-udp
%patch1
%__rm -rf Makefile
%__rm -rf Makefile.in
%__rm -rf */Makefile
%__rm -rf */Makefile.in
%__rm -rf */.deps
%__rm -rf autom4te.cache
%__chmod 0644 *.txt

sed -i 's|inline int     got_block|int     got_block|' include/tsunami-client.h

%build
aclocal
automake --add-missing
autoconf

%configure
%__make clean
%__make %{?jobs:-j%{jobs}}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%__rm \
	 "$RPM_BUILD_ROOT%{_bindir}"/*test \
	 "$RPM_BUILD_ROOT%{_includedir}"/* \
	 "$RPM_BUILD_ROOT%{_libdir}"/*

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc README.txt ChangeLog USAGE.txt
%{_bindir}/tsunami
%{_bindir}/tsunamid
%{_bindir}/rttsunami
%{_bindir}/rttsunamid

%changelog
* Mon May 28 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1+41+349
- Rebuilt for Fedora
* Sun Sep 19 2010 pascal.bleser@opensuse.org
- update to 1.1+41+349
* Fri Mar 19 2010 pascal.bleser@opensuse.org
- initial package
