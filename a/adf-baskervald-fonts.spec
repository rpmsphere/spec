%global fontname adf-baskervald
%global fontconf 60-%{fontname}.conf
%global archivename Baskervald-Std-20150322

Name:    %{fontname}-fonts
Version: 1.020
Release: 1
Summary: Baskervald font of the Arkandis Digital Foundry
Group:     User Interface/X
License:   GPLv2+ with exceptions
URL:       https://arkandis.tuxfamily.org/adffonts.html
Source0:   https://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   https://arkandis.tuxfamily.org/docs/Baskervald-Cat.pdf
Source2:   %{fontname}.metainfo.xml
Source11:  %{name}-fontconfig.conf
BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
This is the Baskervald font of the Arkandis Digital Foundry. This is a serif
collection, intended to mimic the new Baskerville typeface.

%prep
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
for txt in NOTICE.txt */COPYING ; do
   fold -s $txt > $txt.new &&\
   sed -i 's/\r//' $txt.new &&\
   touch -r $txt $txt.new &&\
   mv $txt.new $txt
done

%build

%install
rm -fr %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%clean
rm -fr %{buildroot}

%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc NOTICE.txt OTF/COPYING *.pdf

%changelog
* Tue Jun 19 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.020
- Rebuilt for Fedora
