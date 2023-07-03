%undefine _debugsource_packages
Name:           supybot-bugzilla
Summary:        Plugin for the supybot IRC bot that supports querying Bugzilla
Version:        35
Release:        6.1
Group:          Productivity/Networking/IRC
License:        New BSD Clause
URL:            https://code.google.com/p/supybot-bugzilla/
Requires:       supybot
Source:         Bugzilla-%{version}.tar.bz2
BuildRequires:  python-devel
BuildArch:      noarch

%description
This is a plugin for the supybot IRC bot that supports querying Bugzilla
installations, showing details about bugs, and reading bugmails sent from
Bugzilla to show updates in an IRC channel. It supports working with multiple
Bugzilla installations and can work across many channels and networks.

The main bot using this plugin is "bugbot" on irc.mozilla.org and FreeNode IRC
(though he is called "buggbot" on FreeNode). 

%prep
%setup -q -n Bugzilla-%{version}
sed -i '12s|$|,|' test.py

%build

%install
mkdir -p %buildroot%python2_sitelib/supybot/plugins/Bugzilla
cp -r * %buildroot%python2_sitelib/supybot/plugins/Bugzilla

%clean
rm -fr $RPM_BUILD_ROOT

%files
%doc README.txt
%{python2_sitelib}/supybot/plugins/Bugzilla

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 35
- Rebuilt for Fedora
* Mon Jul 11 2011 lars@linux-schulserver.de
- update to Version 35:
  * The bugmail fields are called "Flags", not "Flag", now.
* Tue May 26 2009 lars@linux-schulserver.de
- initial version
