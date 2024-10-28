Name:       serviio
Version:        0.6.2
Release:        22.1
License:        Free to use
Summary:        A free media server
URL:            https://www.serviio.org/
Group:          Productivity/Multimedia/Other
Source:         %{name}-%{version}-linux.tar.gz
Source1:        serviio.service
Patch1:     serviio_SERVIIO_HOME.patch
BuildRequires:  tar gzip
BuildRequires: systemd
BuildRequires: dos2unix
Requires:   java >= 1.6.0
BuildArch:      noarch

%description
It allows you to stream your media files (music, video 
or images) to renderer devices (e.g. a TV set, Bluray player, games console
or mobile phone) on your connected home network.

%prep
%setup -q
%patch 1 -p1
%__cp %{SOURCE1} .

%build

%install
install -d $RPM_BUILD_ROOT/%{_bindir}
%__cp bin/*.sh $RPM_BUILD_ROOT/%{_bindir}
dos2unix library/derby.properties
chmod -x library/derby.properties

for dir in config lib library plugins; do 
        install -d $RPM_BUILD_ROOT/usr/share/java/serviio/$dir
        %__cp $dir/* $RPM_BUILD_ROOT/usr/share/java/serviio/$dir
done
install -d $RPM_BUILD_ROOT/%{_datadir}/java/serviio/log
install -D -m 644 %{S:1} $RPM_BUILD_ROOT/%{_unitdir}/serviio.service

%pre
/usr/sbin/groupadd -r %{name} 2> /dev/null || :
/usr/sbin/useradd -r -g %{name} -s /bin/false -c "Serviio Daemon" -d /usr/share/java/serviio %{name} 2> /dev/null || :
#service_add_pre serviio.service

%post
#service_add_post serviio.service

%files
%doc legal/Derby-licence.txt legal/FFmpeg-licence.txt legal/FreeMarker-licence.txt legal/Gson-licence.txt legal/HttpCore-licence.txt legal/Jcs-licence.txt legal/JDOM-licence.txt legal/LameMP3Encoder-licence.txt legal/librtmp-licence.txt legal/LICENSE.xerox legal/Log4J-licence.txt legal/Restlet-licence.txt legal/Rome-licence.txt legal/Sanselan-licence.txt legal/slf4j-licence.txt legal/winp-licence.txt legal/XStream-licence.txt LICENCE.txt NOTICE.txt README.txt RELEASE_NOTES.txt
%{_bindir}/serviio.sh
%{_bindir}/serviio-console.sh
%{_unitdir}/serviio.service
%dir %{_datadir}/java/serviio
%dir %{_datadir}/java/serviio/config
%dir %{_datadir}/java/serviio/lib
%dir %{_datadir}/java/serviio/plugins
%{_datadir}/java/serviio/config/*.xml
%{_datadir}/java/serviio/lib/*.jar
%{_datadir}/java/serviio/plugins/*.txt
%attr(775,%{name},%{name}) %{_datadir}/java/serviio/library
%attr(775,%{name},%{name}) %{_datadir}/java/serviio/log

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.2
- Rebuilt for Fedora
