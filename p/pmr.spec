Name:                           pmr
Version:                        1.01
Release:                        2.1
Summary:                        Filter Which Measures Bandwidth and Number of Bytes Passing Through a Pipe
Source:                 https://zakalwe.fi/~shd/foss/pmr/pmr-%{version}.tar.gz
URL:                            https://zakalwe.fi/~shd/foss/pmr/
Group:                  System/Tools
License:                        Public Domain
BuildRequires:  gcc glibc-devel make

%description
pmr is a command line filter that displays the data bandwidth and total number
of bytes passing through a pipe. It can also limit the rate of data going
through the pipe and compute an MD5 checksum of the stream for verifying
data integrity on unreliable networks.

Authors:
--------
    Heikki Orsila <heikki.orsila@iki.fi>

%prep
%setup -q

%build
# not autoconf
./configure --prefix="%{_prefix}" --package-prefix="$RPM_BUILD_ROOT"
%__make \
        %{?jobs:-j%{jobs}} \
        CC="%__cc" \
        CFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 pmr "$RPM_BUILD_ROOT%{_bindir}/pmr"
%__install -D -m0644 doc/pmr.1 "$RPM_BUILD_ROOT%{_mandir}/man1/pmr.1"

%files
%doc AUTHORS COPYING todo.txt
%doc ChangeLog md5.copyright
%{_bindir}/pmr
%doc %{_mandir}/man1/pmr.1*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.01
- Rebuilt for Fedora

* Mon Jan  7 2008 Pascal Bleser <guru@unixtech.be> 1.01
- new upstream version

* Fri Jan  4 2008 Pascal Bleser <guru@unixtech.be> 1.00
- new upstream version

* Mon Oct 22 2007 Pascal Bleser <guru@unixtech.be> 0.12
- moved to openSUSE Build Service

* Thu Feb 15 2007 Pascal Bleser <guru@unixtech.be> 0.12-1
- rewrote spec file
- new upstream version

* Mon Jan  2 2006 Pascal Bleser <guru@unixtech.be> 0.11-1
- new package
