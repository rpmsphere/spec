%define _name elm
%define versionbase 2.5
%define versiontag ME+ 
%define version1 %{versiontag}%{versionbase}
%define minor alpha43
#define release 2
%define ver_full0 %{version1}.%{minor}
%define ver_full %{ver_full0}
%define fix_prefix /usr

Summary: Text-based mailreader supporting MIME, GPG, PGP
Name: elmme
Version: %{versionbase}.%{minor}
Release: 1
URL: http://www.elmme-mailer.org/elm-ME+2.5.html
Source0: http://elmme-mailer.org/elm-ME+2.5/src/%{_name}-%{ver_full0}.tar.gz
License: The Elm(tm) Mail System General Public License
Group: Applications/Communications
Docdir: %{fix_prefix}/doc
Provides: elm

%description
Elm ME+ - an interactive mail system, Millennium Edition.

Elm ME+2.5 is based on Elm 2.4 and incorporates some code from Elm 2.5.
It contains enhanced MIME and character set support. It can read mail
from POP or IMAP folders and can pass mail to the PGP or GPG programs.


%define modargs -M iconv -M smtp -M resolv

%package mod
Summary: Base modules for ELM mail client version %{version1} PL%{minor}
Group: Applications/Communications
requires: %{name} = %{version}

%description mod
Elm ME+ - an interactive mail system, Millennium Edition

libelmme-iconv.so, libelmme-smtp.so and  libelmme-resolv.so modules for 
Elm %{versiontag}%{versionbase}.

The libelmme-smtp.so module is required if /usr/sbin/sendmail is not available.

%package tls
Summary: TLS module for ELM mail client version %{version1} PL%{minor}
Group: Applications/Communications
requires: %{name} = %{version}

%description tls
Elm ME+ - an interactive mail system, Millennium Edition

libelmme-tls.so modules for Elm %{versiontag}%{versionbase}.
This module provides POP's STLS, IMAPs STARTTLS and
SMTPs/submissions  STARTTLS command.
This module uses encryption from OpenSSL library.

%prep
%setup -q -n %{_name}%{versiontag}.%{versionbase}.%{minor}

%build
# Configure seems disable -O2 on Fedore so also _FORTIFY_SOURCE does not work
TEMPOPTIONS=`echo  "$RPM_OPT_FLAGS" | sed 's/ -Wp,-D_FORTIFY_SOURCE[=0-9]* / /'`
cat >config.rpm <<EOM
build_package='define'
optimize="-g $TEMPOPTIONS"
d_shared_rev='.dummy.%{minor}'
soname_include_path=n
use_pmake=n
EOM
sh Configure -b -c config.rpm -P %{fix_prefix}
make all

%install
if [ "$RPM_BUILD_ROOT" != "/" ] ; then
	rm -rf $RPM_BUILD_ROOT
	mkdir -p $RPM_BUILD_ROOT
fi

make package ROOT=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/README.PACKAGE.sh

XX=$RPM_BUILD_ROOT%{_docdir}/%{_name}-%{ver_full}
# We can not let %doc macro to install documentation
# because it install all to one level and clears directory
# on beginning
mkdir -p $XX
install -m 644 README.ME+ $XX/README.ME+
install -m 644 NOTICE $XX/NOTICE
install -m 644 MIME.txt $XX/MIME.txt
mkdir -p $XX/2.4
install -m 644 2.4/Overview $XX/2.4/Overview
install -m 644 2.4/ANNOUNCE.ME $XX/2.4/ANNOUNCE.ME
install -m 644 2.4/ChangeLog.ME $XX/2.4/ChangeLog.ME
install -m 644 2.4/Patchlist $XX/2.4/Patchlist
install -m 644 2.4/Changes $XX/2.4/Changes
install -m 644 2.4/Instruct $XX/2.4/Instruct
install -m 644 2.4/NOTICE $XX/2.4/NOTICE
install -m 644 2.4/README $XX/2.4/README
mkdir -p $XX/doc
install -m 644 doc/elmrc.samp $XX/doc/elmrc.samp
install -m 644 doc/mime.charsets $XX/doc/mime.charsets
install -m 644 doc/mailing.lists $XX/doc/mailing.lists
install -m 644 doc/elmaliases $XX/doc/elmaliases
install -m 644 doc/mime.types $XX/doc/mime.types
install -m 644 doc/terminal.info $XX/doc/terminal.info
install -m 644 doc/mail.services $XX/doc/mail.services
mkdir -p $XX/shared_libs/tls
install -m 644 shared_libs/tls/README.ME+ $XX/shared_libs/tls/README.ME+
mkdir -p $XX/shared_libs/iconv
install -m 644 shared_libs/iconv/README.ME+ $XX/shared_libs/iconv/README.ME+
mkdir -p $XX/shared_libs/smtp
install -m 644 shared_libs/smtp/README.ME+ $XX/shared_libs/smtp/README.ME+
mkdir -p $XX/shared_libs/resolv
install -m 644 shared_libs/resolv/README.ME+ $XX/shared_libs/resolv/README.ME+
# Generate files listing for RPM
#
# main-package
$RPM_BUILD_ROOT%{fix_prefix}/lib/elmregister rpm-list -u root -g root -R $RPM_BUILD_ROOT > XXtmp1
sort XXtmp1 | uniq | sed 's|man1/\(.*\)\.1$|man1/\1.1.gz|' > XXtmp
cp XXtmp $RPM_BUILD_ROOT%{fix_prefix}/lib/elm.filelist-main.rpm
rm XXtmp1
# mod package
$RPM_BUILD_ROOT%{fix_prefix}/lib/elmregister rpm-list -u root -g root -R $RPM_BUILD_ROOT %{modargs} > XXtmp1
sort XXtmp1 | uniq > XXtmp
cp XXtmp $RPM_BUILD_ROOT%{fix_prefix}/lib/elm.filelist-mod.rpm
rm XXtmp1
# tls package
$RPM_BUILD_ROOT%{fix_prefix}/lib/elmregister rpm-list -u root -g root -R $RPM_BUILD_ROOT -M tls > XXtmp1
sort XXtmp1 | uniq > XXtmp
cp XXtmp $RPM_BUILD_ROOT%{fix_prefix}/lib/elm.filelist-tls.rpm
rm XXtmp1
#
# Use temporary location so that installation do not
# overwrite filelist
#
# main-package
$RPM_BUILD_ROOT%{fix_prefix}/lib/elmregister filter -R $RPM_BUILD_ROOT -w $RPM_BUILD_ROOT%{fix_prefix}/lib/elm.filelist-main.%{minor}
# mod package
$RPM_BUILD_ROOT%{fix_prefix}/lib/elmregister filter -R $RPM_BUILD_ROOT %{modargs} -w $RPM_BUILD_ROOT%{fix_prefix}/lib/elm.filelist-mod.%{minor}
# tls package
$RPM_BUILD_ROOT%{fix_prefix}/lib/elmregister filter -R $RPM_BUILD_ROOT -M tls -w $RPM_BUILD_ROOT%{fix_prefix}/lib/elm.filelist-tls.%{minor}
#
rm $RPM_BUILD_ROOT%{fix_prefix}/lib/elm.filelist
%clean
if [ "$RPM_BUILD_ROOT" != "/" ] ; then
	rm -rf $RPM_BUILD_ROOT
fi

%post
# Following files are created or rebuild on replay stage
for F in `%{fix_prefix}/lib/elmconfwriter -l | sed "s/ \(.*\)$//"`
do 
   if [ -f $F ] ; then
	cp -p $F $F.rpmsave
   fi
done
# record only old values before this installation to elm.rc.old-values
F=%{fix_prefix}/lib/elm.rc.old-values
if [ -f $F ] ; then
	mv -f $F $F.rpmsave
fi
err=0
%{fix_prefix}/lib/elmregister replay -F %{fix_prefix}/lib/elm.filelist-main.%{minor} || err=$?
cat %{fix_prefix}/lib/elm.filelist-main.%{minor} >> %{fix_prefix}/lib/elm.filelist
rm %{fix_prefix}/lib/elm.filelist-main.%{minor}
%{fix_prefix}/lib/elmregister unstage
exit $err

%post mod
# mod package postinstall script
err=0
%{fix_prefix}/lib/elmregister replay -F %{fix_prefix}/lib/elm.filelist-mod.%{minor} %{modargs} || err=$?
cat %{fix_prefix}/lib/elm.filelist-mod.%{minor} >> %{fix_prefix}/lib/elm.filelist
rm %{fix_prefix}/lib/elm.filelist-mod.%{minor}
%{fix_prefix}/lib/elmregister unstage %{modargs}
exit $err

%post tls
# tls package postinstall script
err=0
%{fix_prefix}/lib/elmregister replay -F %{fix_prefix}/lib/elm.filelist-tls.%{minor} -M tls || err=$?
cat %{fix_prefix}/lib/elm.filelist-tls.%{minor} >> %{fix_prefix}/lib/elm.filelist
rm %{fix_prefix}/lib/elm.filelist-tls.%{minor}
%{fix_prefix}/lib/elmregister unstage -M tls
exit $err

%preun
# Uninstall if this is is last install
# This assumes that all other elm modules are already uninstalled
if [ $1 = 0 ] ; then
	%{fix_prefix}/lib/elmregister uninstall -M all
fi

%preun mod
# Uninstall if this is is last install
if [ $1 = 0 ] ; then
	%{fix_prefix}/lib/elmregister uninstall %{modargs} 
fi

%preun tls
# Uninstall if this is is last install
if [ $1 = 0 ] ; then
	%{fix_prefix}/lib/elmregister  uninstall -M tls
fi

%postun
if [ $1 = 0 ] ; then
	# We return these files to original places, so that
	# these are used when elm is re-installed
	F=%{fix_prefix}/lib/elm.mimecharsets
	if [ -f $F.rpmsave -a ! -f $F ] ; then
		cp -p $F.rpmsave $F
	fi
	F=%{fix_prefix}/lib/elm.terminalinfo
	if [ -f $F.rpmsave -a ! -f $F ] ; then
		cp -p $F.rpmsave $F
	fi
	F=%{fix_prefix}/lib/elm.mimetypes
	if [ -f $F.rpmsave -a ! -f $F ] ; then
		cp -p $F.rpmsave $F
	fi
        F=%{fix_prefix}/lib/elm.mailinglists
	if [ -f $F.rpmsave -a ! -f $F ] ; then
		cp -p $F.rpmsave $F
	fi
	F=%{fix_prefix}/lib/elm.iso2022sets
	if [ -f $F.rpmsave -a ! -f $F ] ; then
		cp -p $F.rpmsave $F
	fi
        F=%{fix_prefix}/lib/elm.aliases
	if [ -f $F.rpmsave -a ! -f $F ] ; then
		cp -p $F.rpmsave $F
	fi
	F=%{fix_prefix}/lib/elm.mailservices
	if [ -f $F.rpmsave -a ! -f $F ] ; then
		cp -p $F.rpmsave $F
	fi
	F=%{fix_prefix}/lib/elm.rc
	if [ -f $F.rpmsave -a ! -f $F ] ; then
		cp -p $F.rpmsave $F
	fi
	F=%{fix_prefix}/lib/elm.rc.old-values
	rm $F
fi

%postun mod
%{fix_prefix}/lib/elmlibregister -G -I

%postun tls
%{fix_prefix}/lib/elmlibregister -G -I

%files -f %{buildroot}%{fix_prefix}/lib/elm.filelist-main.rpm
%ghost %{fix_prefix}/lib/elm.filelist-main.rpm
%{fix_prefix}/lib/elm.filelist-main.%{minor}
%dir %{_docdir}/%{_name}-%{ver_full}
%doc %{_docdir}/%{_name}-%{ver_full}/README.ME+
%doc %{_docdir}/%{_name}-%{ver_full}/NOTICE
%doc %{_docdir}/%{_name}-%{ver_full}/MIME.txt
%dir %{_docdir}/%{_name}-%{ver_full}/2.4
%doc %{_docdir}/%{_name}-%{ver_full}/2.4/Overview
%doc %{_docdir}/%{_name}-%{ver_full}/2.4/ANNOUNCE.ME
%doc %{_docdir}/%{_name}-%{ver_full}/2.4/ChangeLog.ME
%doc %{_docdir}/%{_name}-%{ver_full}/2.4/Patchlist
%doc %{_docdir}/%{_name}-%{ver_full}/2.4/Changes
%doc %{_docdir}/%{_name}-%{ver_full}/2.4/Instruct
%doc %{_docdir}/%{_name}-%{ver_full}/2.4/NOTICE
%doc %{_docdir}/%{_name}-%{ver_full}/2.4/README
%dir %{_docdir}/%{_name}-%{ver_full}/doc
%doc %{_docdir}/%{_name}-%{ver_full}/doc/elmrc.samp
%doc %{_docdir}/%{_name}-%{ver_full}/doc/mime.charsets
%doc %{_docdir}/%{_name}-%{ver_full}/doc/mailing.lists
%doc %{_docdir}/%{_name}-%{ver_full}/doc/elmaliases
%doc %{_docdir}/%{_name}-%{ver_full}/doc/mime.types
%doc %{_docdir}/%{_name}-%{ver_full}/doc/terminal.info
%doc %{_docdir}/%{_name}-%{ver_full}/doc/mail.services
%dir %{_docdir}/%{_name}-%{ver_full}/shared_libs

%files mod -f %{buildroot}%{fix_prefix}/lib/elm.filelist-mod.rpm
%ghost %{fix_prefix}/lib/elm.filelist-mod.rpm
%{fix_prefix}/lib/elm.filelist-mod.%{minor}
%dir %{_docdir}/%{_name}-%{ver_full}/shared_libs/iconv
%doc %{_docdir}/%{_name}-%{ver_full}/shared_libs/iconv/README.ME+
%dir %{_docdir}/%{_name}-%{ver_full}/shared_libs/smtp
%doc %{_docdir}/%{_name}-%{ver_full}/shared_libs/smtp/README.ME+
%dir %{_docdir}/%{_name}-%{ver_full}/shared_libs/resolv
%doc %{_docdir}/%{_name}-%{ver_full}/shared_libs/resolv/README.ME+

%files tls -f %{buildroot}%{fix_prefix}/lib/elm.filelist-tls.rpm
%ghost %{fix_prefix}/lib/elm.filelist-tls.rpm
%{fix_prefix}/lib/elm.filelist-tls.%{minor}
%dir %{_docdir}/%{_name}-%{ver_full}/shared_libs/tls
%doc %{_docdir}/%{_name}-%{ver_full}/shared_libs/tls/README.ME+

%changelog
* Thu Oct 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5me.alpha42
- Rebuild for Fedora
* Sat Oct 26 2013 Kari Hurtta <deb@elmme-mailer.org>
- Initial package
