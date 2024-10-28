%undefine _debugsource_packages

Summary:        Openfire XMPP Server
Name:           openfire
Version:        4.1.2
Release:        9.1
BuildRequires:  ant java-devel-openjdk lua
Requires:       java
#Source0:       https://www.igniterealtime.org/downloadServlet?filename=openfire/%{name}_src_4_1_2.tar.gz
Source0:        %{name}_src_4_1_2.txz
Source1:        https://repo1.maven.org/maven2/javax/activation/activation/1.1.1/activation-1.1.1.jar
Group:          Applications/Communications
License:        GPL
URL:            https://www.igniterealtime.org/
Patch0:         openfire-sysvinit.patch
Patch1:         openfire-3.7.0-SSLConfig.patch
Patch2:         openfire-3.7.0-IPv6-workaround.patch
%define         prefix /usr/share
%define         homedir %{prefix}/openfire

%description
Openfire is a leading Open Source, cross-platform IM server based on the
XMPP (Jabber) protocol. It has great performance, is easy to setup and use,
and delivers an innovative feature set.

%package doc
Summary:    Openfire XMPP Server Documentation
Group:      Documentation/Other
BuildArch:  noarch

%description doc
This package contains optional documentation provided in addition to
this package's base documentation.

%prep
%setup -q -n %{name}_src
%patch 0 -p1
#patch1 -p0
%patch 2 -p0
sed -i 's|"1\.9"|"17"|' build/build.xml
cp %{SOURCE1} build/lib

%build
# Build Tasks
cd build
# Default | openfire
ant openfire
# Specific Plugins
ant -Dplugin=search plugin
cd ..

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true

# Prep the install location.
mkdir -p $RPM_BUILD_ROOT%{prefix}

# Copy over the main install tree.
cp -R target/openfire $RPM_BUILD_ROOT%{homedir}

# Set up distributed JRE
#pushd $RPM_BUILD_ROOT%{homedir}
#gzip -cd %{SOURCE1} | tar xvf -
#popd

# Set up the init script.
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp $RPM_BUILD_ROOT%{homedir}/bin/extra/redhat/openfire $RPM_BUILD_ROOT/etc/init.d/openfire
chmod 755 $RPM_BUILD_ROOT/etc/init.d/openfire
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
ln -s -f %{_sysconfdir}/init.d/%{name} $RPM_BUILD_ROOT%{_sbindir}/rc%{name}

# Make the startup script executable.
chmod 755 $RPM_BUILD_ROOT%{homedir}/bin/openfire.sh

# Set up the sysconfig file.
#mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
#cp $RPM_BUILD_ROOT%{homedir}/bin/extra/redhat/openfire-sysconfig $RPM_BUILD_ROOT/etc/sysconfig/openfire
mkdir -p $RPM_BUILD_ROOT%/var/adm/fillup-templates/
install -D $RPM_BUILD_ROOT%{homedir}/bin/extra/redhat/openfire-sysconfig $RPM_BUILD_ROOT/var/adm/fillup-templates/sysconfig.openfire
chmod -x $RPM_BUILD_ROOT/var/adm/fillup-templates/sysconfig.openfire

# Copy over the documentation | Not needed with the new openfire-doc package
#cp -R documentation $RPM_BUILD_ROOT%{homedir}/documentation
#cp changelog.html $RPM_BUILD_ROOT%{homedir}/
#cp LICENSE.html $RPM_BUILD_ROOT%{homedir}/
#cp README.html $RPM_BUILD_ROOT%{homedir}/

# Copy over the i18n files
cp -R resources/i18n $RPM_BUILD_ROOT%{homedir}/resources/i18n

# Make sure scripts are executable
chmod 755 $RPM_BUILD_ROOT%{homedir}/bin/extra/openfired
chmod 755 $RPM_BUILD_ROOT%{homedir}/bin/extra/redhat-postinstall.sh

# Move over the embedded db viewer pieces
mv $RPM_BUILD_ROOT%{homedir}/bin/extra/embedded-db.rc $RPM_BUILD_ROOT%{homedir}/bin
mv $RPM_BUILD_ROOT%{homedir}/bin/extra/embedded-db-viewer.sh $RPM_BUILD_ROOT%{homedir}/bin

# We don't really need any of these things.
rm -rf $RPM_BUILD_ROOT%{homedir}/bin/extra
rm -f $RPM_BUILD_ROOT%{homedir}/bin/*.bat
rm -rf $RPM_BUILD_ROOT%{homedir}/resources/nativeAuth/osx-ppc
rm -rf $RPM_BUILD_ROOT%{homedir}/resources/nativeAuth/solaris-sparc
rm -rf $RPM_BUILD_ROOT%{homedir}/resources/nativeAuth/win32-x86
rm -f $RPM_BUILD_ROOT%{homedir}/lib/*.dll
rm -rf $RPM_BUILD_ROOT%{homedir}/resources/spank

# Dont enable fdupes (on resources/security/) as it breaks the crypto store
# See: https://www.igniterealtime.org/issues/browse/OF-30
# For now disabled completely..
#%fdupes -s $RPM_BUILD_ROOT

%files
 %defattr(-,daemon,daemon)
%attr(750, daemon, daemon) %dir %{homedir}
%dir %{homedir}/bin
%{homedir}/bin/openfire.sh
%attr(750, daemon, daemon) %{homedir}/bin/openfirectl
%config(noreplace) %{homedir}/bin/embedded-db.rc
%{homedir}/bin/embedded-db-viewer.sh
%dir %{homedir}/conf
%config(noreplace) %{homedir}/conf/*
%dir %{homedir}/lib
%{homedir}/lib/*.jar
%{homedir}/lib/log4j.xml
%dir %{homedir}/logs
%{homedir}/plugins
%dir %{homedir}/resources
%dir %{homedir}/resources/database
%{homedir}/resources/database/*.sql
%dir %{homedir}/resources/database/upgrade
%dir %{homedir}/resources/database/upgrade/*
%{homedir}/resources/database/upgrade/*/*
%dir %{homedir}/resources/i18n
%{homedir}/resources/i18n/*
%dir %{homedir}/resources/nativeAuth
%dir %{homedir}/resources/nativeAuth/linux-i386
%{homedir}/resources/nativeAuth/linux-i386/*
%dir %{homedir}/resources/security
%config(noreplace) %{homedir}/resources/security/keystore
%config(noreplace) %{homedir}/resources/security/truststore
%config(noreplace) %{homedir}/resources/security/client.truststore
#%doc %{homedir}/documentation
#%doc %{homedir}/LICENSE.html 
#%doc %{homedir}/README.html 
#%doc %{homedir}/changelog.html
%{_sbindir}/rc%{name}
%{_sysconfdir}/init.d/openfire
#%config(noreplace) %{_sysconfdir}/sysconfig/openfire
%config(noreplace) /var/adm/fillup-templates/sysconfig.openfire
#%{homedir}/jre

%files doc
%doc documentation/docs/* LICENSE.html README.html changelog.html

%changelog
* Mon Feb 20 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.2
- Rebuilt for Fedora
* Tue Jan 26 2010 nix@opensuse.org
- Dont enable fdupes (on resources/security/) as it breaks the crypto store
  See: https://www.igniterealtime.org/issues/browse/OF-30
  For now disabled completely..
* Tue Jan 19 2010 nix@opensuse.org
- Add openfire-3.6.4-self_signed_certificate.patch from to fix SSL
  cert problem: https://www.igniterealtime.org/issues/browse/OF-30
* Fri Oct 23 2009 nix@opensuse.org
- Change java dependency to "java-sun >=1.6.0" so that SLES 11 works properly
* Fri Jun 19 2009 claes.backstrom@fsfe.org
- New upstrean 3.6.4
  Openfire New Features
  * Use stronger RSA encryption algorithm for certificates
    creation.
  Openfire Bug Fixes
  * Prevent users from changing other users passwords.
  * LdapGroups assumed all members never in AltBaseDN.
  * Stacktrace of exception while initializing SSLConfig are
    now logged.
  * DefaultAdminProvider was not including default admin account
    when there were no admins specified.
* Wed Apr 29 2009 claes.backstrom@fsfe.org
- New upstream 3.6.3
- Handle sysconfig file correctly
- Created rcopenfire symlink
- Moved to /usr/share for openSUSE 11.1 and later
* Thu Apr 23 2009 maw@pobox.com
- Replace openfirect.patch with openfire-sysvinit.patch, which
  patches the file necessary to allow openfire to build on
  openSUSE 11.1.
  Wed Jan 07 22:18:00 UTC 2008 - Peter Nixon
- Patch init script to add LSB compliant headers (to build on openSUSE 11.1+)
- Add rpm prereq line to silence rpmlint
* Sat Nov 22 2008 claes.backstrom@fsfe.org
- New upstream 3.6.2
* Wed Aug 27 2008 claes.backstrom@fsfe.org
- New upstream release 3.6.0
* Wed Jul  9 2008 claes.backstrom@fsfe.org
- New upstream release 3.5.2
* Thu Feb 14 2008 claes.backstrom@fsfe.org
- New Upstream Release 3.4.5
    Openfire New Features
  * Improved connection pool recovery logic by switching to proxool.
  * Now possible to allow the same component to connect many times to the same JVM.
    Openfire Bug Fixes
  * Fixed small memory leak in Multi User Chat.
  * LDAP settings (particularly search filters) will no longer get corrupted upon saving.
  * SSL settings pages now handle broken keystores without crashing.
  * Added JID to room search results.
  * Setting VM options from config file in Debian now works.
  * RPM is no longer throwing warnings about ci and jivedev users.
  * Debian postinstall is now checking to make sure openfire group exists.
* Sun Jan 20 2008 claes.backstrom@fsfe.org
- New Upstream Release 3.4.4
  * Jetty upgraded to fix announced security issue (https://www.kb.cert.org/vuls/id/553235)
  * LDAP vCard database storage fixed to work properly with Active Directory and others. !!NOTE!! API Changes for providers were required. See important notes below. (1 vote)
  * Can now delete an avatar when using LDAP.
  * Current LDAP settings now being kept when editing config from admin interface.
  * Openfire install directories, log directories, etc are no longer world readable. (1 vote)
  * RPM uninstall no longer fails if Openfire not currently running.
* Wed Jan  9 2008 claes.backstrom@fsfe.org
- Initial package
