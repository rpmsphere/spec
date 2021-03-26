Name:         zsync
Summary:      RSYNC over HTTP
URL:          http://zsync.moria.org.uk/
Group:        Networking
License:      Artistic
Version:      0.6.2
Release:      4.1
Source0:      http://zsync.moria.org.uk/download/zsync-%{version}.tar.bz2

%description
zsync is a file transfer program. It allows you to download a
file from a remote server, where you have a copy of an older
version of the file on your computer already. zsync downloads only
the new parts of the file. It uses the same algorithm as rsync.
However, where rsync is designed for synchronising data from one
computer to another within an organisation, zsync is designed for
file distribution, with one file on a server to be distributed to
thousands of downloaders. zsync requires no special server software
just a web server to host the files and imposes no extra load on the
server, making it ideal for large scale file distribution.

%prep
%setup -q

%build
autoreconf -ifv
#endian="-DLITTLE_ENDIAN=0 -DBIG_ENDIAN=1 -DBYTE_ORDER=0"
CPPFLAGS="%{optflags} $endian" \
LDFLAGS="%{optflags}" \
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir}
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_datadir}/doc/%{name}
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.2
- Rebuild for Fedora
