import { StartDsfrOnHydration } from "../dsfr-bootstrap";

export default function Page() {
  return (
    <>
      {/* Important: You must mount this component on every pages of your App! */}
      <StartDsfrOnHydration />
      <h1>Welcome!</h1>
    </>
  );
}
