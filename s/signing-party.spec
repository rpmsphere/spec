Name:           signing-party
Version:        1.1.4
Release:        23.1
Summary:        GPG Tools
License:        GPL-2.0+
Group:          Productivity/Security
URL:            https://packages.debian.org/sid/signing-party
Source:         https://ftp.debian.org/debian/pool/main/s/signing-party/signing-party_%{version}.orig.tar.gz
# PATCH-FIX-OPENSUSE caff-manpage.patch [bnc#722626]
Patch1:         caff-manpage.patch
Requires:       /usr/sbin/sendmail
Requires:       gpg
Requires:       perl
Requires:       perl-GnuPG-Interface
Requires:       perl-MIME-tools
Requires:       perl-MailTools
Requires:       perl-Text-Template
BuildRequires:  perl-podlators
Requires:       qprint
# We are not including keyanalyze which gets compiled and therefore
# the package is noarch
BuildArch:      noarch

%description
PGP Tools is a collection for all kinds of pgp related things, including
signing scripts, party preparation scripts etc.

caff is a script that helps you in keysigning. It takes a list of
keyids on the command line, fetches them from a keyserver and calls
GnuPG so that you can sign it. It then mails each key to all its email
addresses - only including the one UID that we send to in each mail.

pgp-clean takes a list of keyids on the command line and outputs an
ascii-armored keyring on stdout for each key with all signatures
except self-signatures stripped. Its use is to reduce the size of keys
sent out after signing. (pgp-clean is a stripped-down caff version.)

gpg-key2ps will output a PostScript file which has your Key-ID, UIDs
and fingerprint nicely formatted for printing paper slips to take with
you to a signing-party.

Given one or more key-ids, gpg-mailkeys mails these keys to their
owners. You use this after you've signed them. By default, the mails
contain a standard text and your name and address as the From (as
determined by the sendmail command).

gpglist takes a keyid and creates a listing showing who signed your
user IDs.

gpgsigs was written to assist the user in signing keys during a
keysigning party. It takes as input a file containing keys in gpg
--list-keys format and prepends every line with a tag indicating if
the user has already signed that uid.

keylookup is a wrapper around gpg --search, allowing you to search for
keys on a keyserver. It presents the list of matching keys to the user
and allows her to select the keys for importing into the GnuPG
keyring.

%prep
%setup -qn signing-party-%{version}
%patch1 -p1

%build
cp -f /usr/share/automake-*/config.guess keyanalyze/pgpring/
make CFLAGS="%{optflags}"

%install
mkdir -p $RPM_BUILD_ROOT
install -d d $RPM_BUILD_ROOT%{_bindir}
install -m 755 caff/caff caff/pgp-clean caff/pgp-fixkey $RPM_BUILD_ROOT%{_bindir}
install -m 755 gpglist/gpglist $RPM_BUILD_ROOT%{_bindir}
install -m 755 gpg-key2ps/gpg-key2ps $RPM_BUILD_ROOT%{_bindir}
install -m 755 gpglist/gpglist $RPM_BUILD_ROOT%{_bindir}
install -m 755 gpg-mailkeys/gpg-mailkeys $RPM_BUILD_ROOT%{_bindir}
install -m 755 gpgsigs/gpgsigs $RPM_BUILD_ROOT%{_bindir}
install -m 755 keylookup/keylookup $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 caff/caff.1 caff/pgp-clean.1 caff/pgp-fixkey.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 gpg-key2ps/gpg-key2ps.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 gpglist/gpglist.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 gpg-mailkeys/gpg-mailkeys.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 gpgsigs/gpgsigs.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 keylookup/keylookup.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc caff/README caff/README.gpg-agent caff/README.many-keys caff/README.v3-keys caff/caffrc.sample
%doc gpgsigs/gpgsigs-lt2k5*.txt  gpg-mailkeys/example.gpg-mailkeysrc
%doc keylookup/NEWS
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.4
- Rebuilt for Fedora
* Thu Mar 22 2012 cfarrell@suse.com
- license update: GPL-2.0+
  Various Open Source Licenses is not acceptable as a spec file license.
  For this package, GPL-2.0+ seems to be the most accurate license choice
* Wed Mar 14 2012 joop.boonen@opensuse.org
- Build version 1.1.4
  * gpg-key2ps:
    + Apply patch from Uwe Kleine-König to deal with latin1 characters
  * gpg-mailkeys:
    + Correct path of ~/.gpg-mailkeysrc and ~/.signature in manpage.
    + Add new environment variable SENDMAIL_ARGS to allow user to pass
    arguments to sendmail
  * caff:
    + Correct path of ~/.caffrc in informational messages
    + Be more verbose on unexpected key ID
    + Refactor import of own key and import for keys to sign from keyrings.
    + Also automatically import keys to sign from the user's normal gpg
    keyrings.
    + Use --no-auto-check-trustdb when importing keys from files or
    the user's normal gpg keyrings
    + manpage: Refer to all of /usr/share/doc/signing-party/caff/ and not
    just to /usr/share/doc/signing-party/caff/caffrc.sample
    + Fix horrible &function calls used because of broken prototypes.
    + Even if all keys to sign were found in the user's normal gpg
    keyrings we still need to import them (again) from any keyrings
    passed with --key-files - the keys there might be newer, containing
    new subkeys (for encryption), uids (for signing) or revocations.
    + Make importing of keys to be signed from the normal gpg optional
    (--keys-from-gnupg).
    + refactor copying of command line options into global config variable.
    + Create the mail files in ~/.caff/keys even if mail is not sent
* Wed Oct 12 2011 aj@suse.de
- Fix caff manpage (bnc#722626)
- Run spec file through spec-cleaner
* Tue Oct 26 2010 aj@suse.de
- Make package noarch.
* Mon Jun 28 2010 joop.boonen@opensuse.org
- Build version 1.1.3
* Sat Sep 19 2009 aj@suse.de
- Fix Requires.
* Wed Aug 12 2009 aj@suse.de
- Update to version 1.1.1.
- Many bugfixes.
- New tools: keyanalyze, sig2dot, springgraph.
- Drop keylookup.
* Sat Mar  3 2007 aj@suse.de
- Add missing requires for caff.
- Update to version 0.4.9.
* Wed Sep 13 2006 aj@suse.de
- Initial package.
