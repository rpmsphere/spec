Name: aseqjoy
Summary: Joystick to ALSA MIDI Sequencer Converter
URL: http://terminatorx.org/aseqjoy.html
Version: 0.0.1
Release: 3.1
License: GPLv2
Group: Hardware/Joystick
BuildRequires: alsa-lib-devel
Source:    %name-%version.tar.gz

%description
aseqjoy uses the ALSA sequencer API to emit the MIDI events. Therefore it
creates an output port named after joystick used. You can then use for example
aconnect (from alsa-utils) or Robert Ham's alsa-patch-bay to connect an aseqjoy
instance to an input port of your choice.

Each axis of the joystick device is mapped to a specific MIDI controller.
Moving the joystick along an axis will cause aseqjoy to emit MIDI controller
messages via ALSA's sequencer API. The value of the controller message
represents the joystick's position along the axis (eg 'left' -> 0, 'middle' ->
63, 'right' -> 127).

%prep
%setup -q

%build
%{configure}
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog README
%doc %{_mandir}/man1/%{name}*
%{_bindir}/%{name}

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuild for Fedora
* Mon Mar 29 2010 lenz@grimmer.com
- Initial version for the openSUSE build service (0.0.1)
