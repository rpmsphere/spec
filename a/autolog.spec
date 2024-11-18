Summary:        Auto logout daemon - chase sleeping users
Name:           autolog
Version:        0.40
Release:        1
License:        GPL
URL:            https://www.cip-bau.uni-hannover.de/~juerges
Group:          Daemons
Source:         autolog-0.40.tar.gz

%description
This program wakes up from time to time and looks around for users
doing nothing. If they seem to be idle for too much time long, they
get a warning message. They get some time to type something into a
terminal, otherwise they get kicked off.
This programs automatically logs out "forgotten" logins.

It is also possible to set a maximum session time for a special user,
group, etc. If a users exceeds that he will be banned for a certain
amount of time.

This programm is also looking for lost processes
and kills them from time to time. if (500<uid<60000).

The program was derived from (autolog) by Kyle Bates.

Authors:
--------
    Kyle Bateman <kyle@actarg.com> (autolog <0.40)
    Carsten Juerges <juerges@cip-bau-uni-hannover.de> (autolog 0.40)

%prep
%setup -q
sed -i '518,527s|rpb\.|rpb.__|' autolog.c
sed -i '65i #include <ctype.h>\n#include <stdlib.h>' autolog.c

%build
sed -i 's|^CFLAGS.*|CFLAGS = -g -Wno-implicit-int -Wno-implicit-function-declaration -Wno-return-mismatch -Wno-incompatible-pointer-types|' Makefile
rm autolog
make autolog

%install
sed -i 's| /| %{buildroot}/|' Makefile
mkdir -p %{buildroot}/etc %{buildroot}/sbin/init.d %{buildroot}/usr/sbin %{buildroot}/var/log %{buildroot}/usr/man/man8 %{buildroot}/usr/man/man5
make install

%files
%config /etc/autolog.conf
/sbin/init.d/autolog
/usr/sbin/autolog
/var/log/autolog.log
#/tmp/autolog.data
%doc README CHANGES
%doc /usr/man/man5/autolog.conf.5.gz
%doc /usr/man/man8/autolog.8.gz

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.40
- Rebuilt for Fedora
* Fri Apr 28 2000 autolog <juerges@cip-bau.uni-hannover.de>
- Version 0.40 released. First public release.
  The whole thing renamed to the old name, to show this is
  an upgraded version of autolog an not an entiryly new
  thing.
  Many things to complete, but this should already work.
* Wed Apr 12 2000 autologd <juerges@cip-bau.uni-hannover.de>
- Version 0.10 released. First release for discussion
  purpose with the other author(s). So someone else
  could check, whether it works.
  Many things to complete, but this should already work
