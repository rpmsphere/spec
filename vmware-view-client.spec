%global debug_package %{nil}

%filter_provides_in %{_libdir}
%filter_from_requires /libudev.so.0/d
%filter_from_requires /libssl.so.0.9.8/d
%filter_from_requires /libcrypto.so.0.9.8/d
%filter_setup

Name:           vmware-view-client
Version:        2.2.0
Release:        1%{?dist}.bin
Summary:        Deliver rich, personalized virtual desktops with VMware View 5

License:        Proprietary
URL:            http://www.vmware.com/
Source0:        http://archive.canonical.com/ubuntu/pool/partner/v/vmware-view-client/vmware-view-client_%{version}.orig.tar.gz
Source1:        vmware-view.sh
Source2:        vmware-view-client.desktop
Source3:        vmware-view-client.png
Source4:        vmware-view-client-addons.zip

ExclusiveArch:	i686

BuildRequires:  desktop-file-utils

Requires:       freerdp >= 1.0.2
Requires:       adwaita-gtk2-theme%{?_isa}
Requires:       alsa-plugins-pulseaudio%{?_isa}
Requires:       libcanberra-gtk2%{_isa}
Requires:       libcanberra-gtk3%{_isa}
Requires:       PackageKit-gtk3-module%{_isa}

%description
The VMware View Client for Linux, optimized for VMware View 5, turns your
Linux PC into a thin client and connects you to your company's Virtual
Desktop Infrastructure. With VMware View 5 PCoIP capabilities you can
deliver a personalized high fidelity experience for end-users across
sessions, devices, operating systems, and legacy applications.

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
tar --extract --directory %{buildroot} --strip-components=1 --file %{SOURCE0}

mv %{buildroot}/%{_bindir}/vmware-view %{buildroot}/%{_libdir}/vmware/vmware-view
unzip %{SOURCE4} -d %{buildroot}/%{_libdir}/vmware

cp -a %{SOURCE1} %{buildroot}/%{_bindir}/vmware-view
chmod u=rwx,og=rx %{buildroot}/%{_bindir}/vmware-view

mkdir -p %{buildroot}%{_libdir}/vmware/view/pkcs11

mkdir ./doc
mv %{buildroot}%{_datadir}/doc/vmware-view-client/* ./doc
rmdir %{buildroot}%{_datadir}/doc/vmware-view-client
rmdir %{buildroot}%{_datadir}/doc

ln -s ../libudev.so.1 %{buildroot}%{_libdir}/vmware/libudev.so.0

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -a %{SOURCE3} %{buildroot}%{_datadir}/pixmaps

%find_lang vmware-view

%files -f vmware-view.lang
%doc doc/*

%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
%{_bindir}/vmware-remotemks
%{_bindir}/vmware-view
%{_bindir}/vmware-view-log-collector
%{_bindir}/vmware-view-tunnel
%{_bindir}/vmware-remotemks-container
%{_libdir}/libpcoip_crypto.so
%{_libdir}/libpcoip_crypto_non_fips.so
%{_libdir}/libpcoip_client.so
%{_libdir}/pcoip
%{_libdir}/vmware

%changelog
* Mon Jul 21 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.0-2
- Rebuild for Fedora

* Wed Mar  6 2013 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.7.0.0-2
- Bring in some more runtime requirements to make sure we have sound
- and eliminate a couple annoying error messages.

* Wed Mar  6 2013 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.7.0.0-1
- First version
