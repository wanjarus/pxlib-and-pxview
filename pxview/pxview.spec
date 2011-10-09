Summary: Program to read and convert Paradox DB files
Name: pxview
Version: 0.2.5
Release: 1
Copyright: see doc/COPYING
Group: Applications/Utils
Url: http://pxlib.sourceforge.net/
Packager: Uwe Steinmann <uwe@steinmann.cx>
Source: http://prdownloads.sourceforge.net/pxlib/pxview-%{PACKAGE_VERSION}.tar.gz
BuildRoot: /var/tmp/rpm/pxview-root
Prefix: /usr

%description
pxview is a simple program based on pxlib to read and convert Paradox DB files.
Possible conversions are to csv and sql. pxview can also read blob data and
write each object to a single file.

%prep
%setup

%build
./configure --prefix=%prefix --with-sqlite --mandir=%prefix/share/man --infodir=%prefix/share/info
make

%install
rm -rf ${RPM_BUILD_ROOT}
install -d -m 755 ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install
(cd ${RPM_BUILD_ROOT}/usr/bin; ln -s pxview px2sql; ln -s pxview px2csv; ln -s pxview px2html; ln -s pxview px2sqlite)

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%attr(-,root,root) %doc README AUTHORS ChangeLog COPYING INSTALL
%attr(-,root,root) %{prefix}/bin/*
%attr(-,root,root) %{prefix}/share/man/man1/*
