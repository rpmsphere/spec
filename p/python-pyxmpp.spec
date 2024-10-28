Name:                   python-pyxmpp
Version:                1.1.1
Release:                6.1
Summary:                Python Jabber/XMPP Implementation
Source:                 https://pyxmpp.jajcus.net/downloads/pyxmpp-%{version}.tar.gz
Patch1:                 %{name}-libxml2_not_in_usr_local.patch
URL:                    https://pyxmpp.jajcus.net/
Group:                  Development/Libraries/Python
License:                GNU Library General Public License (LGPL)
BuildRequires:  python2-devel libxml2-devel
#BuildRequires:  python2-dns

%description
PyXMPP is a Python XMPP (RFC 3920,3921) and Jabber
(https://www.jabber.org/protocol/) implementation. It is based on libxml2 --
fast and fully-featured XML parser.

PyXMPP provides most core features of the XMPP protocol and several
JSF-defined extensions. PyXMPP provides building blocks for creating Jabber
clients and components. Developer uses them to setup XMPP streams, handle
incoming events and create outgoing stanzas (XMPP "packets").

%prep
%setup -q -n pyxmpp-%{version}
%patch 1

%build
python2 ./setup.py build

%install
python2 ./setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc ChangeLog CHANGES COPYING README TODO examples
%{python2_sitearch}/*

%changelog
* Sun Jun 30 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuilt for Fedora
* Tue Apr 27 2010 pascal.bleser@opensuse.org
- update to 1.1.1
* Wed Oct  3 2007 jfunk@funktronics.ca
- Checking in to sync cicount. For some reason, the i586 package had a higher
  release number than the x86_64 package
* Sun Jun 10 2007 guru@unixtech.be
- initial build service submission
