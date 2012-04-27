Name:			fotoxx
Version:		12.05
Release:		1
Summary:		Editor of image files from digital cameras
License:		GPLv3
Group:			Graphics
Source0:		http://kornelix.squarespace.com/storage/downloads/%{name}-%{version}.tar.gz
URL:			http://kornelix.squarespace.com/fotoxx/
BuildRequires:		pkgconfig(gtk+-3.0)
BuildRequires:		ufraw
BuildRequires:		perl-Image-ExifTool
BuildRequires:		tiff-devel
BuildRequires:		xdg-utils
BuildRequires:		imagemagick
Requires:		exiv2
Requires:		ufraw
Requires:		perl-Image-ExifTool

%description
Edit image files from a digital camera. Includes color and contrast
enhancement, red-eye removal, sharpen, crop, rotate, noise removal,
HDR (high dynamic range) and panorama image compositing, thumbnail
image browser, tag editing and search.

%prep
%setup -q

%build
%make CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}" PREFIX=%{_prefix}

%install
%__make PREFIX=%{buildroot}%{_prefix} install

# menu icon
for size in 16 24 32 48 64 128
do
%__install -D -m 644 %{buildroot}%{_datadir}/%{name}/icons/%{name}${size}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/%{name}.png
done

# (tpg) drop upstream desktop file
rm -rf %{buildroot}%{_datadir}/applications/kornelix-fotoxx.desktop

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Version=1.0
Name=%{name}
GenericName=Image Editor
Comment=Edit image files from a digital camera
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;X-MandrivaLinux-CrossDesktop;
EOF

%files
%defattr(-,root,root)
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/fotoxx.1*
