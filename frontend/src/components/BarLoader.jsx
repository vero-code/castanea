import { motion } from "framer-motion";

const variants = {
  initial: {
    scaleX: 0.5,
    opacity: 0,
  },
  animate: {
    scaleX: 1,
    opacity: 1,
    transition: {
      repeat: Infinity,
      repeatType: "mirror",
      duration: 1,
      ease: "circIn",
    },
  },
};

const BarLoader = () => {
  return (
    <motion.div
      transition={{ staggerChildren: 0.25 }}
      initial="initial"
      animate="animate"
      className="flex gap-2 items-end"
      style={{ padding: "20px", backgroundColor: "rgba(255,255,255,0.6)", borderRadius: "8px" }}
    >
      {[...Array(5)].map((_, i) => (
        <motion.div
          key={i}
          variants={variants}
          style={{
            backgroundColor: "#6c3cff",
            width: "8px",
            height: "48px",
            borderRadius: "4px"
          }}
        />
      ))}
    </motion.div>
  );
};

export default BarLoader;