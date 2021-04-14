Name: pyurlsnooper
Summary: To locate the urls of audio and video files
Version: 1.4
Release: 3.1
Group: Applications/Internet
License: PD
URL: http://sourceforge.net/projects/pyurlsnooper/
Source0: http://sourceforge.net/projects/pyurlsnooper/files/%{name}_v%{version}.tar.gz
Requires: pcapy, python-impacket, pygtk2
BuildArch: noarch

%description
This is a OS independent equivalent of URL Snooper from http://www.donationcoder.com/
(similar to https://sourceforge.net/projects/mediasniffer/). Can be used in combination
with RTMPDump (http://rtmpdump.mplayerhq.hu/) in order to capture streams.

%prep
%setup -q -n %{name}

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
install %{name}* PyLib.py %{buildroot}%{_datadir}/%{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files
%doc CHANGES README
%{_datadir}/%{name}

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
