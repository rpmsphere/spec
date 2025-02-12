%undefine _debugsource_packages
%global ezcgi /var/www/cgi-bin
%global rcdir /etc/ezmlm

Name: ezmlm-idx
Version: 7.0.2
Release: 1
Summary: Easy Mailing List Manager + IDX patches
License: GPL
Group: Utilities/System
BuildRequires: mysql-devel
BuildRequires: postgresql-devel
BuildRequires: groff
Source0: https://ezmlm.org/archive/%{version}/%{name}-%{version}.tar.gz
Source1: %{name}-zh_TW.tar.gz
URL: https://www.ezmlm.org

%description
ezmlm lets users set up their own mailing lists within qmail's address
hierarchy. A user, Joe, types

   ezmlm-make ~/SOS ~/.qmail-sos joe-sos isp.net

and instantly has a functioning mailing list, joe-sos@isp.net, with all
relevant information stored in a new ~/SOS directory.

ezmlm sets up joe-sos-subscribe and joe-sos-unsubscribe for automatic
processing of subscription and unsubscription requests. Any message to
joe-sos-subscribe will work; Joe doesn't have to explain any tricky
command formats. ezmlm will send back instructions if a subscriber sends
a message to joe-sos-request or joe-sos-help.

ezmlm automatically archives new messages. Messages are labelled with
sequence numbers; a subscriber can fetch message 123 by sending mail to
joe-sos-get.123. The archive format supports fast message retrieval even
when there are thousands of messages.

ezmlm takes advantage of qmail's VERPs to reliably determine the
recipient address and message number for every incoming bounce message.
It waits ten days and then sends the subscriber a list of message
numbers that bounced. If that warning bounces, ezmlm sends a probe; if
the probe bounces, ezmlm automatically removes the subscriber from the
mailing list.

ezmlm is easy for users to control. Joe can edit ~/SOS/text/* to change
any of the administrative messages sent to subscribers. He can remove
~/SOS/public and ~/SOS/archived to disable automatic subscription and
archiving. He can put his own address into ~/SOS/editor to set up a
moderated mailing list. He can edit ~/SOS/{headeradd,headerremove} to
control outgoing headers. ezmlm has several utilities to manually
inspect and manage mailing lists.

ezmlm uses Delivered-To to stop forwarding loops, Mailing-List to
protect other mailing lists against false subscription requests, and
real cryptographic cookies to protect normal users against false
subscription requests. ezmlm can also be used for a sublist,
redistributing messages from another list.

ezmlm is reliable, even in the face of system crashes. It writes each
new subscription and each new message safely to disk before it reports
success to qmail.

ezmlm doesn't mind huge mailing lists. Lists don't even have to fit into
memory. ezmlm hashes the subscription list into a set of independent
files so that it can handle subscription requests quickly. ezmlm uses
qmail for blazingly fast parallel SMTP deliveries.

The IDX patches add: Indexing, (Remote) Moderation, digest, make
patches, multi-language, MIME, global interface, SQL database support.

%description -l pl
Menad<BF>er pocztowych list dyskusyjnych, ca<B3>kowicie spolszczony, mo<BF>liwo
<B6><F6> zdalnego moderowania, MIME.

%package mysql
Summary: MySQL support module for ezmlm-idx
Group: Utilities/System 
Requires: ezmlm-idx
Conflicts: ezmlm ezmlm-idx-std ezmlm-idx-mysql < 6.0

%description mysql
MySQL support module for ezmlm-idx

%package pgsql
Summary: PostgreSQL support module for ezmlm-idx
Group: Utilities/System 
Requires: ezmlm-idx
Conflicts: ezmlm ezmlm-idx-std ezmlm-idx-pgsql < 6.0

%description pgsql
PostgreSQL support module for ezmlm-idx

%package cgi
Prefix: %ezcgi
Summary: www archiver for %name
Group: Utilities/System 
Requires: ezmlm-idx

%description cgi
www archiver for %name.
 
%prep 
%setup -q
tar zxf %{SOURCE1} -C lang
sed -i 's/pt_BR/zh_TW/g' ETC FILES Makefile SOURCES TARGETS
sed -i 's|LD|LD -Wl,--allow-multiple-definition|' make-load.sh

%build 
echo %rcdir >conf-etc
echo %_bindir >conf-bin
echo %_mandir >conf-man
echo %_libdir/ezmlm >conf-lib
echo gcc %optflags -I%_includedir/mysql -I%_includedir/pgsql >conf-cc
echo gcc %optflags -s -L/usr/lib/mysql >conf-ld

make it man install mysql pgsql

%install
/bin/rm -rf %buildroot

mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_libdir/ezmlm
mkdir -p %buildroot/%_mandir
mkdir -p %buildroot/%rcdir
mkdir -p %buildroot/%ezcgi 

# Do not create cat subdirs on Linux
%ifos Linux
sed '/cat/d' MAN > MAN.tmp
mv MAN.tmp MAN
%else
%endif

./install %buildroot/%rcdir < ETC
./install %buildroot/%_bindir < BIN
./install %buildroot/%_mandir < MAN
./install %buildroot/%_libdir/ezmlm < LIB
ln -s `head -n 1 conf-lang` %buildroot/%rcdir/default

cp ezmlm-cgi %buildroot/%ezcgi

# create file list for man pages (without ezmlm-cgi.1)
find %buildroot/%_mandir -type f \
| sed -e "s}%buildroot}}" -e "s}$}*}" > man-list

cp ezmlm-cgi.1 %buildroot/%_mandir/man1
chmod 644 %buildroot/%_mandir/man1/ezmlm-cgi.1

# Create INSTALL file for how to set up ezcgi
cat <<EOF > INSTALL.cgi
The script ezmlm-cgi is installed as  %ezcgi/ezmlm-cgi with 
permissions 0444.  In order to use it, you need to make it
SUID root.  So do

chmod 4755 %ezcgi/ezmlm-cgi

Please see INSTALL 16-22) in this package's doc directory and the
man page ezmlm-cgi.1 for more details on setting up and using ezmlm-cgi.

EOF

%post
echo To create an ezmlmrc file for a language other than US English
echo go to this package\'s doc directory, and type 
echo "    make iso"
echo 'where "iso" is the ISO language designation.' 
echo For currently supported languages, see the INSTALL
echo file, section 7.

%files -f man-list
%dir %rcdir
%config(noreplace) %rcdir/*
%doc BLURB CHANGES* FAQ INSTALL README*
%doc THANKS TODO UPGRADE ChangeLog
%doc DOWNGRADE ezmlmrc.template
%_bindir/*
%_libdir/ezmlm/sub-std.so

%files cgi
%doc INSTALL.cgi ezcgirc ezcgi.css
%attr(0444,root,root) %ezcgi/*
%_mandir/man1/ezmlm-cgi.1*

%files mysql
%_libdir/ezmlm/sub-mysql.so

%files pgsql
%_libdir/ezmlm/sub-pgsql.so

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 7.0.2
- Rebuilt for Fedora
