Name:           flvstreamer
Version:        2.1c1
Release:        3.1
Summary:        Open source command line RTMP client
License:        GPLv2+
Group:          Networking/File transfer
URL:            https://savannah.nongnu.org/projects/flvstreamer
Source:         https://download.savannah.gnu.org/releases/%{name}/source/%{name}-%{version}.tar.gz

%description
Flvstreamer is an open source command-line RTMP client intended to stream
audio or video content from all types of flash or rtmp servers. Forked from
rtmpdump v1.6 with encrypted rtmp and swf verification support removed. This
tool provides free interoperability with the previously undocumented adobe
RTMP protocol so widely in use on the internet today. It was developed
entirely by reverse engineering methods and without access to any proprietary
or restrictive-license protocol specifications.

%prep
%setup -q -n %{name}

%build
%__make posix OPT="%optflags" XLDFLAGS="%{?ldflags}"

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
find -type f -perm -u+x | xargs install -m755 -t $RPM_BUILD_ROOT%{_bindir}

%files
%doc README ChangeLog
%{_bindir}/flvstreamer
%{_bindir}/streams
%{_bindir}/rtmpsrv
%{_bindir}/rtmpsuck

%changelog
* Mon Jul 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1c1
- Rebuilt for Fedora

* Sat Oct 22 2011 shlomif <shlomif> 2.1c1-1.mga2
+ Revision: 157349
- imported package flvstreamer

* Sat Oct 22 2011 Barry Jackson <zen25000[at]zen.co.uk> 2.1c1-1mga2
- Imported for Mageia

* Sat Mar 06 2010 Anssi Hannula <anssi@mandriva.org> 2.1c1-1mdv2010.1
+ Revision: 515296
- new version

* Tue Jul 21 2009 RaphaM-CM-+l Gertz <rapsys@mandriva.org> 1.8e-3mdv2010.0
+ Revision: 398407
- Remove contextual arch build
- Add doc README
- Update flvstreamer release
- Add flvstreamer source and spec file
- Rename package name
- Rename package
- Created package structure for rtpmdump.
